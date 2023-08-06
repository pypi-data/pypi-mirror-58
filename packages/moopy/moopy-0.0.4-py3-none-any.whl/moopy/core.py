# Copyright 2019-- Derk Kappelle
#
# This file is part of MooPy, a Python package with
# Multi-Objective Optimization (MOO) tools.
#
# MooPy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# MooPy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with MooPy.  If not, see <http://www.gnu.org/licenses/>.
from __future__ import absolute_import, division, print_function

import sys
import copy
import math
import time
import logging
import datetime
import warnings
import operator
import functools
import itertools
import numpy as np
from scipy.optimize import minimize, curve_fit
from scipy.optimize.optimize import OptimizeResult, vecnorm
from abc import ABCMeta, abstractmethod

from cachetools import cached, TTLCache
cache = TTLCache(maxsize=10000, ttl=1000)
cache2 = TTLCache(maxsize=10000, ttl=1000)

LOGGER = logging.getLogger("MooPy")
EPSILON = sys.float_info.epsilon
POSITIVE_INFINITY = float("inf")


class MooPyError(Exception):
    pass


class Problem(object):

    def __init__(self, funs, ds_ini, lims, cons, jac, options, *args, **kwargs):

        super(Problem, self).__init__()

        if not isinstance(ds_ini, list):
            self.x0 = np.asarray(ds_ini, dtype=float)
        else:
            self.x0 = np.asarray(ds_ini[0], dtype=float)
        self.nvars = len(self.x0)

        if not isinstance(funs, FunctionWrapper):
            self.funcs = FunctionWrapper(funs)
        else:
            self.funcs = funs
        if not isinstance(lims, LimitWrapper):
            self.limits = LimitWrapper(lims, self.nvars)
        else:
            self.limits = lims
        if not isinstance(cons, ConstraintWrapper):
            self.constraints = ConstraintWrapper(cons)
        else:
            self.constraints = cons
        if not isinstance(jac, JacobianWrapper):
            self.jac = JacobianWrapper(self.funcs.funcs_ini, jac)
        else:
            self.jac = jac

        if options is None:
            self.options = {}
        else:
            self.options = dict(options)

        self.tol = self.options.pop('tol', 1e-6)

    def __call__(self, solution):
        """Evaluate the solution.

        This method is responsible for decoding the decision variables,
        invoking the evaluate method, and updating the solution.

        Parameters
        ----------
        solution: Solution
            The solution to evaluate.
        """
        problem = solution.problem
        solution.variables[:] = [problem.types[i].decode(solution.variables[i]) for i in range(problem.nvars)]

        self.evaluate(solution)

        solution.variables[:] = [problem.types[i].encode(solution.variables[i]) for i in range(problem.nvars)]
        solution.constraint_violation = sum(
            [abs(f(x)) for (f, x) in zip(solution.problem.constraints, solution.constraints)])
        solution.feasible = solution.constraint_violation == 0.0
        solution.evaluated = True

    def evaluate(self, solution):
        """Evaluates the problem.

        By default, this method calls the function passed to the constructor.
        Alternatively, a problem can subclass and override this method.  When
        overriding, this method is responsible for updating the objectives
        and constraints stored in the solution.

        Parameters
        ----------
        solution: Solution
            The solution to evaluate.
        """
        if self.function is None:
            raise MooPyError("function not defined")

        if self.nconstrs > 0:
            (objs, constrs) = self.function(solution.variables)
        else:
            objs = self.function(solution.variables)
            constrs = []

        if not hasattr(objs, "__getitem__"):
            objs = [objs]

        if not hasattr(constrs, "__getitem__"):
            constrs = [constrs]

        if len(objs) != self.nobjs:
            raise MooPyError("incorrect number of objectives: expected %d, received %d" % (self.nobjs, len(objs)))

        if len(constrs) != self.nconstrs:
            raise MooPyError(
                "incorrect number of constraints: expected %d, received %d" % (self.nconstrs, len(constrs)))

        solution.objectives[:] = objs
        solution.constraints[:] = constrs


class MultipleRun(Problem):

    __metaclass__ = ABCMeta

    def __init__(self,
                 funs,
                 ds_ini,
                 lims,
                 cons,
                 jac,
                 options,
                 *args,
                 **kwargs):

        super(MultipleRun, self).__init__(funs, ds_ini, lims, cons, jac, options, *args, **kwargs)

        self.prt_info = self.options.get('print_info', False)

        self.ds = []
        self.it = 1
        self.Npar = int(self.options.pop('Npar', 20))

        self.condition = self.options.get('termination', int(1e5))

        if isinstance(self.condition, int):
            self.condition = MaxEvaluations(self.condition)

        if isinstance(self.condition, TerminationCondition):
            self.condition.initialize(self)

    def method_info(self):

        self.eveness = Eveness(self.ds)

        if self.prt_info:
            print('Number of single function evaluations:', self.funcs.num_sing_eva)
            print('Number of Jacobian evaluations:', self.jac.num_grad_eva)
            print('Number of iterations:', self.it)
            print('Number of Pareto points:', len(self.ds))


        return [self.funcs.num_sing_eva, self.jac.num_grad_eva, self.it, len(self.ds), self.eveness]

    def get_dp(self, x):
        return ParetoPoint(f=self.funcs.evaluate_funcs(x), x=x, g=self.constraints.evaluate_cons(x))

    @abstractmethod
    def initialize_method(self):
        raise NotImplementedError("method not implemented")

    @abstractmethod
    def perform_SOOP(self, dp):
        raise NotImplementedError("method not implemented")

    def run(self, callback=None):

        start_time = time.time()

        LOGGER.log(logging.INFO, "%s starting", type(self).__name__)

        while not self.condition(self) and self.it < self.Npar - 1:

            # Define and solve SOOP
            dp_es = self.perform_SOOP(self.ds[-1])

            # Add point to data set
            self.ds.append(dp_es)

            # Iteration count and check for infinite loops
            self.it += 1

            if callback is not None:
                callback(self)

        LOGGER.log(logging.INFO,
                   "%s finished; Total NFE: %d, Elapsed Time: %s",
                   type(self).__name__,
                   self.funcs.num_sing_eva,
                   datetime.timedelta(seconds=time.time() - start_time))

        return self.ds, self.method_info()


class WS(MultipleRun):
    __metaclass__ = ABCMeta

    def __init__(self,
                 funs,
                 ds_ini,
                 lims,
                 cons,
                 jac,
                 options,
                 *args,
                 **kwargs):

        super(WS, self).__init__(funs, ds_ini, lims, cons, jac, options, *args, **kwargs)

        self.ds_ini = []
        for xi in ds_ini:
            self.ds_ini.append(self.get_dp(xi))

    def initialize_method(self):

        self.delta = 1 / self.Npar

        a = 0.
        self.l = []
        for i in range(self.Npar):
            self.l.append([(1-a), a])
            a += self.delta

    def perform_SOOP(self, dp):

        funs = self.funcs.combine_funcs(self.l[self.it])
        lims = self.limits.lims_ini
        cons = self.constraints.con_ini

        res = minimize(funs,
                       dp.x,
                       bounds=lims,
                       constraints=cons)

        if not res.success:
            raise MooPyError('solving the SOOP failed')

        if np.all(dp.x == res.x):
            return dp
        else:
            return self.get_dp(res.x)

    def solve(self):
        LOGGER.log(logging.INFO, "%s initialise", type(self).__name__)
        self.initialize_method()

        self.ds.append(self.ds_ini[0])

        return self.run()


class EC(MultipleRun):
    __metaclass__ = ABCMeta

    def __init__(self,
                 funs,
                 ds_ini,
                 lims,
                 cons,
                 jac,
                 options,
                 *args,
                 **kwargs):

        super(EC, self).__init__(funs, ds_ini, lims, cons, jac, options, *args, **kwargs)

        self.ds_ini = []
        for xi in ds_ini:
            self.ds_ini.append(self.get_dp(xi))

    def initialize_method(self):

        self.v = []
        for i, dp in enumerate(self.ds_ini):
            if i != 1:
                self.v.append(self.ds_ini[1].f - dp.f)

        self.delta = self.v[0][0] / self.Npar
        a = self.ds_ini[0].f[0]

        self.l = []
        for i in range(self.Npar):
            self.l.append(a)
            a += self.delta

    def perform_SOOP(self, dp):

        funs = self.funcs.single_func(1)
        lims = self.limits.lims_ini

        con = [{'type': 'ineq', 'fun': lambda x: self.l[self.it] - self.funcs.single_func(0)(x), }]
        cons = self.constraints.add_constraint(con)

        res = minimize(funs,
                       dp.x,
                       bounds=lims,
                       constraints=cons)

        if not res.success:
            x_try = self.limits.upb * np.random.random_sample(dp.x.shape) - self.limits.lob
            res = minimize(self.funcs.single_func(1), x_try, bounds=self.limits.lims_ini,
                           constraints=cons, jac=self.jac.single_grad(1))
            if not res.success:
                pass

        if np.all(dp.x == res.x):
            return dp
        else:
            return self.get_dp(res.x)

    def solve(self):
        LOGGER.log(logging.INFO, "%s initialise", type(self).__name__)
        self.initialize_method()

        self.ds.append(self.ds_ini[0])

        return self.run()


class NC(MultipleRun):
    __metaclass__ = ABCMeta

    def __init__(self,
                 funs,
                 ds_ini,
                 lims,
                 cons,
                 jac,
                 options,
                 *args,
                 **kwargs):

        super(NC, self).__init__(funs, ds_ini, lims, cons, jac, options, *args, **kwargs)

        self.ds_ini = []
        for xi in ds_ini:
            self.ds_ini.append(self.get_dp(xi))

    def initialize_method(self):

        self.v = []
        for i, dp in enumerate(self.ds_ini):
            if i != 1:
                self.v.append(self.ds_ini[1].f - dp.f)

        self.delta = 1 / self.Npar
        a1 = 1.
        a2 = 0.
        self.p = []
        for i in range(self.Npar):
            self.p.append(a1 * self.ds_ini[0].f + a2 * self.ds_ini[1].f)
            a1 -= self.delta
            a2 += self.delta

    def perform_SOOP(self, dp):

        con = [{'type': 'ineq', 'fun': lambda x: -np.dot(self.v[0], (self.funcs.evaluate_funcs(x) - self.p[self.it]))}]
        if self.jac.jac_ini == '2-point' or self.jac.jac_ini == '3-point':
            con[0]['jac'] = self.jac.jac_ini
        cons = self.constraints.add_constraint(con)

        res = minimize(self.funcs.single_func(1),
                       dp.x,
                       bounds=self.limits.lims_ini,
                       constraints=cons)

        if not res.success:
            x_try = self.limits.upb * np.random.random_sample(dp.x.shape) - self.limits.lob
            res = minimize(self.funcs.single_func(1), x_try, bounds=self.limits.lims_ini,
                           constraints=cons, jac=self.jac.single_grad(1))
            if not res.success:
                pass

        if np.all(dp.x == res.x):
            return dp
        else:
            return self.get_dp(res.x)

    def solve(self):
        LOGGER.log(logging.INFO, "%s initialise", type(self).__name__)
        self.initialize_method()

        self.ds.append(self.ds_ini[0])

        return self.run()


class ApproxExtra(Problem):
    __metaclass__ = ABCMeta

    def __init__(self,
                 funs,
                 ds_ini,
                 lims,
                 cons,
                 jac,
                 options,
                 *args,
                 **kwargs):

        super(ApproxExtra, self).__init__(funs, ds_ini, lims, cons, jac, options, *args, **kwargs)

        self.prt_info = self.options.get('print_info', False)

        self.ds = []
        self.it = 1
        self.Npar = 0

        self.condition = self.options.get('termination', int(1e5))

        if isinstance(self.condition, int):
            self.condition = MaxEvaluations(self.condition)

        if isinstance(self.condition, TerminationCondition):
            self.condition.initialize(self)

    def method_info(self):

        self.eveness = Eveness(self.ds)

        if self.prt_info:
            print('Number of single function evaluations:', self.funcs.num_sing_eva)
            print('Number of Jacobian evaluations:', self.jac.num_grad_eva)
            print('Number of iterations:', self.it)
            print('Number of Pareto points:', len(self.ds))

        return [self.funcs.num_sing_eva, self.jac.num_grad_eva, self.it, len(self.ds), self.eveness]

    def get_dp(self, x):
        return ParetoPoint(f=self.funcs.evaluate_funcs(x), x=x, g=self.constraints.evaluate_cons(x))

    ###########################################################################################
    # Checks
    def check_x(self, x):
        # Check input x
        for i, y in enumerate(x <= self.limits.lob + self.tol):
            if y:
                x[i] = self.limits.lob[i]

        for i, y in enumerate(x >= self.limits.upb - self.tol):
            if y:
                x[i] = self.limits.upb[i]

        return x

    def check_finished(self, dp):
        if np.all(dp.f[0] <= self.ds[-1].f[0]) or np.all(dp.f[1] >= self.ds[-1].f[1]) \
                or np.isclose(dp.f[1], self.ds[-1].f[1]):
            return True

    def check_finished2(self, dp):
        if np.all((np.abs(self.ds_ini[1].x - dp.x)) < 0.1 * self.dx):
            return True
        if vecnorm(self.ds_ini[1].f - dp.f) < 0.001:
            return True
        if np.all(dp.f > self.ds_ini[1].f):
            return True

    def get_act_bounds(self, dp):
        return list(dp.x <= self.limits.lob + self.tol) + \
               list(dp.x >= self.limits.upb - self.tol) + \
               list(dp.g <= 0 + self.tol)

    def check_nonsmooth(self, dp):
        if self.it == 1:
            self.act_bounds = self.get_act_bounds(dp)
            return False
        else:
            return self.act_bounds != self.get_act_bounds(dp)

    ###########################################################################################
    # SOOP function
    def SOOP_EC(self, x):

        dp = self.get_dp(x)

        # g_i(x) >= 0, i = 1, ..., m

        con = [{'type': 'ineq', 'fun': lambda x: dp.f[0] - self.funcs.single_func(0)(x), }]
        # if self.jac.jac_ini == '2-point' or self.jac.jac_ini == '3-point': %%%%%%%%'jac': self.jac.single_grad_neg(1)
        #     con[0]['jac'] = self.jac.jac_ini jac=self.jac.single_grad(0)

        cons = self.constraints.add_constraint(con)

        res = minimize(self.funcs.single_func(1), dp.x, bounds=self.limits.lims_ini,
                       constraints=cons, )

        if np.all(dp.x == res.x):
            return dp
        else:
            return self.get_dp(res.x)

    def finish_PSE(self, dp):
        return self.ds, self.method_info()

    def finish_PSE2(self, dp):

        if self.finish_min:
            res = minimize(self.funcs.single_func(1), self.ds[-1].x, bounds=self.limits.lims_ini,
                           constraints=self.constraints.con_ini, jac=self.jac.single_grad(1))

            if not res.success:
                raise ValueError

            if np.all(self.ds[-1].x == res.x):
                return self.ds, self.method_info()
            else:
                self.ds.append(self.get_dp(res.x))

        return self.ds, self.method_info()

    @abstractmethod
    def initialize_method(self):
        raise NotImplementedError("method not implemented")

    @abstractmethod
    def perform_SOOP(self, dp):
        raise NotImplementedError("method not implemented")

    @abstractmethod
    def inital_step(self, dp):
        raise NotImplementedError("method not implemented")

    @abstractmethod
    def general_step(self, dp):
        raise NotImplementedError("method not implemented")

    def run(self, callback=None):

        start_time = time.time()

        LOGGER.log(logging.INFO, "%s starting", type(self).__name__)

        while not self.condition(self):

            if self.it == 1:

                x_es = self.inital_step(self.ds[-1])

            else:

                x_es = self.general_step(self.ds[-1])

            x_es = self.check_x(x_es)
            dp = self.perform_SOOP(x_es)

            if self.check_finished(dp):
                LOGGER.log(logging.INFO,
                           "%s finished; Total NFE: %d, Elapsed Time: %s",
                           type(self).__name__,
                           self.funcs.num_sing_eva,
                           datetime.timedelta(seconds=time.time() - start_time))
                return self.finish_PSE(dp)

            elif self.check_nonsmooth(dp):
                self.it = 1
                self.ds.append(dp)
            else:
                self.ds.append(dp)
                self.it += 1

            if callback is not None:
                callback(self)

        LOGGER.log(logging.INFO,
                   "%s finished; Total NFE: %d, Elapsed Time: %s",
                   type(self).__name__,
                   self.funcs.num_sing_eva,
                   datetime.timedelta(seconds=time.time() - start_time))

        return self.ds, self.method_info()


class PSE(ApproxExtra):
    __metaclass__ = ABCMeta

    def __init__(self,
                 funs,
                 ds_ini,
                 lims,
                 cons,
                 jac,
                 options,
                 *args,
                 **kwargs):

        super(PSE, self).__init__(funs, ds_ini, lims, cons, jac, options, *args, **kwargs)

        self.ds_ini = []
        for xi in ds_ini:
            self.ds_ini.append(self.get_dp(xi))

    ###########################################################################################
    # Curve fit functions and their derivatives
    def first_poli_func(self, x, a, b):
        return a + b * x

    def der_first_poli_func(self, x, a, b):
        return b

    def second_poli_func(self, x, a, b, c):
        return a + b * x + c * x ** 2

    def der_second_poli_func(self, x, a, b, c):
        return b + 2 * c * x

    def third_poli_func(self, x, a, b, c, d):
        return a + b * x + c * x ** 2 + d * x ** 3

    def der_third_poli_func(self, x, a, b, c, d):
        return b + 2 * c * x + 3 * d * x ** 2

    def sine_func(self, x, a, b, c, d):
        return a * (np.sin(2 * np.pi * x / b + 2 * np.pi / c)) + d

    ###########################################################################################
    # functions for Curve fitting
    def do_curve_fit(self, ddata, xdata, params, pord=None):
        if pord is None:
            pord = self.fit_func
        if pord == 'pol1':
            return curve_fit(self.first_poli_func, ddata, xdata, params[:2])
        elif pord == 'pol2':
            return curve_fit(self.second_poli_func, ddata, xdata, params[:3])
        elif pord == 'pol3':
            return curve_fit(self.third_poli_func, ddata, xdata, params[:4])
        elif pord == 'sine':
            return curve_fit(self.sine_func, ddata, xdata, params[:4])

    def get_params_ini(self, data, npar=None):
        if npar is None:
            npar = self.npar
        if hasattr(data, '__len__'):
            params = np.ones((len(data), npar))
        else:
            params = np.ones((1, npar))
        params[:, 0] = data
        return params

    def get_npar(self, pord):
        if pord == 'pol1':
            return 2
        elif pord == 'pol2':
            return 3
        elif pord == 'pol3':
            return 4
        elif pord == 'sine':
            return 4

    def get_pord(self, npar):
        if npar == 2:
            return 'pol1'
        elif npar == 3:
            return 'pol2'
        elif npar == 4:
            return 'pol3'
        elif npar == 4:
            return 'sine'

    def apprd(self, d, params, pord=None):
        if pord is None:
            pord = self.fit_func
        if pord == 'pol1':
            return self.first_poli_func(d, params[:, 0], params[:, 1])
        elif pord == 'pol2':
            return self.second_poli_func(d, params[:, 0], params[:, 1], params[:, 2])
        elif pord == 'pol3':
            return self.third_poli_func(d, params[:, 0], params[:, 1], params[:, 2], params[:, 3])
        elif pord == 'sine':
            return self.sine_func(d, params[:, 0], params[:, 1], params[:, 2], params[:, 3])

    def appdrd(self, d, params, pord=None):
        if pord is None:
            pord = self.fit_func
        if pord == 'pol1':
            return self.der_first_poli_func(d, params[:, 0], params[:, 1])
        elif pord == 'pol2':
            return self.der_second_poli_func(d, params[:, 0], params[:, 1], params[:, 2])
        elif pord == 'pol3':
            return self.der_third_poli_func(d, params[:, 0], params[:, 1], params[:, 2], params[:, 3])

    def do_appr(self, ddata, xdata, params):
        # Seclecting the curve fit function based on the number of data points.
        if len(ddata) < self.npar:
            npar = len(ddata)  # number of parameters
        else:
            npar = self.npar
        pord = self.get_pord(npar)  # curve function type

        # Do curve fit through x data based on d for each x_i
        for i in range(self.nvars):
            params[i, :npar], pcov = self.do_curve_fit(ddata, xdata[:, i], params[i, :], pord=pord)

        return params, pord

    ###########################################################################################
    # Calculate axtrapolation step
    def dd_c(self, *args):
        return self.dx

    def dd_dx(self, drda, *args):
        return np.dot(np.abs(drda), np.abs(self.dx)) / (vecnorm(drda) ** 2)

    def dd_df(self, drda, dp, *args):
        if not hasattr(dp, 'jac'):
            dp.jac = self.jac.evaluate_jac(dp.x)
        dfrda = np.dot(dp.jac, drda)
        return np.dot(np.abs(dfrda), np.abs(self.dx)) / (vecnorm(dfrda) ** 2)

    ###########################################################################################
    # PSE initialization
    def initialize_method(self):

        self.fit_func = self.options.pop('fit_func', 'pol2')
        self.npar = self.get_npar(self.fit_func)
        self.nsamp = self.options.pop('nsample', 5)
        self.Npar = self.options.pop('Npar', 20)
        self.tol = self.options.pop('tol', 1e-6)
        self.finish_min = self.options.pop('finish_min', True)
        self.prt_info = self.options.get('print_info', False)
        self.prt_steps = self.options.get('print_steps', False)

        dd_method = self.options.pop('dd_method', {})
        if not isinstance(dd_method, dict):
            dd_method = dict(dd_method)

        if not dd_method:
            self.dx = (self.limits.upb - self.limits.lob) / self.Npar
            self.cal_dd = self.dd_dx
        elif 'c' in dd_method:
            self.dx = dd_method['c']
            self.cal_dd = self.dd_c
        elif 'dx'in dd_method:
            self.dx = dd_method['dx']
            self.cal_dd = self.dd_dx
        elif 'df'in dd_method:
            self.dx = dd_method['df']
            self.cal_dd = self.dd_df
        else:
            raise ValueError

        self.d1 = self.options.pop('d1', 0.1)
        self.d2 = self.options.pop('d2', 0.1)

        SOOP_options = self.options.pop('SOOP_options', {})
        if not isinstance(SOOP_options, dict):
            SOOP_options = dict(SOOP_options)

        if not SOOP_options:
            self.perform_SOOP = self.SOOP_EC
            self.restricted = False
        else:
            if 'SOOP_method' in SOOP_options:
                SOOP_method = SOOP_options['SOOP_method']
                if SOOP_method == 'NC':
                    self.perform_SOOP = self.SOOP_EC
                elif callable(SOOP_method):
                    self.perform_SOOP = SOOP_method
                else:
                    self.perform_SOOP = self.SOOP_EC
            else:
                self.perform_SOOP = self.SOOP_EC
            if 'Restricted' in SOOP_options:
                self.restricted = SOOP_options['Restricted']
            else:
                self.restricted = False

    def inital_step(self, dp):

        self.ddata = [0]
        self.xda = [self.ds[-1].x]
        self.params = self.get_params_ini(self.xda[0], npar=self.npar)

        jac = self.jac.evaluate_jac(dp.x)

        return  dp.x - self.d1 * (jac[1] / vecnorm(jac[1]))

    def general_step(self, dp):
        # Update curve fit data.
        self.xda.append(self.ds[-1].x)
        self.ddata.append(self.ddata[-1] + vecnorm(self.xda[-2] - self.xda[-1]))
        if len(self.xda) > self.nsamp:
            del self.xda[0]
            del self.ddata[0]
            self.params[:, 0] = self.xda[0]
        xdata = np.asarray(self.xda, dtype=np.float64)

        # Do curve fitting
        self.params, pord = self.do_appr(self.ddata, xdata, self.params)

        # Decrease the first step size in case of inadequate approximation.
        if len(self.ddata) < self.npar:
            dd = 0.1 * self.d2
        else:
            dd = self.d2

        # Get x_es at approximated distance.
        return self.apprd((self.ddata[-1] + dd), self.params, pord=pord)

    def solve(self):
        LOGGER.log(logging.INFO, "%s initialise", type(self).__name__)
        self.initialize_method()

        self.ds.append(self.ds_ini[0])

        return self.run()


class PSEVariableStep(ApproxExtra):
    __metaclass__ = ABCMeta

    def __init__(self,
                 funs,
                 ds_ini,
                 lims,
                 cons,
                 jac,
                 options,
                 *args,
                 **kwargs):

        super(PSEVariableStep, self).__init__(funs, ds_ini, lims, cons, jac, options, *args, **kwargs)

        self.ds_ini = []
        for xi in ds_ini:
            self.ds_ini.append(self.get_dp(xi))

    ###########################################################################################
    # Curve fit functions and their derivatives
    def first_poli_func(self, x, a, b):
        return a + b * x

    def der_first_poli_func(self, x, a, b):
        return b

    def second_poli_func(self, x, a, b, c):
        return a + b * x + c * x ** 2

    def der_second_poli_func(self, x, a, b, c):
        return b + 2 * c * x

    def third_poli_func(self, x, a, b, c, d):
        return a + b * x + c * x ** 2 + d * x ** 3

    def der_third_poli_func(self, x, a, b, c, d):
        return b + 2 * c * x + 3 * d * x ** 2

    def sine_func(self, x, a, b, c, d):
        return a * (np.sin(2 * np.pi * x / b + 2 * np.pi / c)) + d

    ###########################################################################################
    # functions for Curve fitting
    def do_curve_fit(self, ddata, xdata, params, pord=None):
        if pord is None:
            pord = self.fit_func
        if pord == 'pol1':
            return curve_fit(self.first_poli_func, ddata, xdata, params[:2])
        elif pord == 'pol2':
            return curve_fit(self.second_poli_func, ddata, xdata, params[:3])
        elif pord == 'pol3':
            return curve_fit(self.third_poli_func, ddata, xdata, params[:4])
        elif pord == 'sine':
            return curve_fit(self.sine_func, ddata, xdata, params[:4])

    def get_params_ini(self, data, npar=None):
        if npar is None:
            npar = self.npar
        if hasattr(data, '__len__'):
            params = np.ones((len(data), npar))
        else:
            params = np.ones((1, npar))
        params[:, 0] = data
        return params

    def get_npar(self, pord):
        if pord == 'pol1':
            return 2
        elif pord == 'pol2':
            return 3
        elif pord == 'pol3':
            return 4
        elif pord == 'sine':
            return 4

    def get_pord(self, npar):
        if npar == 2:
            return 'pol1'
        elif npar == 3:
            return 'pol2'
        elif npar == 4:
            return 'pol3'
        elif npar == 4:
            return 'sine'

    def apprd(self, d, params, pord=None):
        if pord is None:
            pord = self.fit_func
        if pord == 'pol1':
            return self.first_poli_func(d, params[:, 0], params[:, 1])
        elif pord == 'pol2':
            return self.second_poli_func(d, params[:, 0], params[:, 1], params[:, 2])
        elif pord == 'pol3':
            return self.third_poli_func(d, params[:, 0], params[:, 1], params[:, 2], params[:, 3])
        elif pord == 'sine':
            return self.sine_func(d, params[:, 0], params[:, 1], params[:, 2], params[:, 3])

    def appdrd(self, d, params, pord=None):
        if pord is None:
            pord = self.fit_func
        if pord == 'pol1':
            return self.der_first_poli_func(d, params[:, 0], params[:, 1])
        elif pord == 'pol2':
            return self.der_second_poli_func(d, params[:, 0], params[:, 1], params[:, 2])
        elif pord == 'pol3':
            return self.der_third_poli_func(d, params[:, 0], params[:, 1], params[:, 2], params[:, 3])

    def do_appr(self, ddata, xdata, params):
        # Seclecting the curve fit function based on the number of data points.
        if len(ddata) < self.npar:
            npar = len(ddata)  # number of parameters
        else:
            npar = self.npar
        pord = self.get_pord(npar)  # curve function type

        # Do curve fit through x data based on d for each x_i
        for i in range(self.nvars):
            params[i, :npar], pcov = self.do_curve_fit(ddata, xdata[:, i], params[i, :], pord=pord)

        return params, pord

    ###########################################################################################
    # Calculate axtrapolation step
    def dd_c(self, *args):
        return self.dx

    def dd_dx(self, drda, *args):
        return np.dot(np.abs(drda), np.abs(self.dx)) / (vecnorm(drda) ** 2)

    def dd_df(self, drda, dp, *args):
        if not hasattr(dp, 'jac'):
            dp.jac = self.jac.evaluate_jac(dp.x)
        dfrda = np.dot(dp.jac, drda)
        return np.dot(np.abs(dfrda), np.abs(self.dx)) / (vecnorm(dfrda) ** 2)

    ###########################################################################################
    # PSE initialization
    def initialize_method(self):

        self.fit_func = self.options.pop('fit_func', 'pol2')
        self.npar = self.get_npar(self.fit_func)
        self.nsamp = self.options.pop('nsample', 5)
        self.Npar = self.options.pop('Npar', 20)
        self.tol = self.options.pop('tol', 1e-6)
        self.finish_min = self.options.pop('finish_min', True)
        self.prt_info = self.options.get('print_info', False)

        dd_method = self.options.pop('dd_method', {})
        if not isinstance(dd_method, dict):
            dd_method = dict(dd_method)

        if not dd_method:
            self.dx = (self.limits.upb - self.limits.lob) / self.Npar
            self.cal_dd = self.dd_dx
        elif 'c' in dd_method:
            self.dx = dd_method['c']
            self.cal_dd = self.dd_c
        elif 'dx' in dd_method:
            self.dx = dd_method['dx']
            self.cal_dd = self.dd_dx
        elif 'df' in dd_method:
            self.dx = dd_method['df']
            self.cal_dd = self.dd_df
        else:
            raise ValueError

        SOOP_options = self.options.pop('SOOP_options', {})
        if not isinstance(SOOP_options, dict):
            SOOP_options = dict(SOOP_options)

        if not SOOP_options:
            self.perform_SOOP = self.SOOP_EC
            self.restricted = False
        else:
            if 'SOOP_method' in SOOP_options:
                SOOP_method = SOOP_options['SOOP_method']
                if SOOP_method == 'NC':
                    self.perform_SOOP = self.SOOP_EC
                elif callable(SOOP_method):
                    self.perform_SOOP = SOOP_method
                else:
                    self.perform_SOOP = self.SOOP_EC
            else:
                self.perform_SOOP = self.SOOP_EC
            if 'Restricted' in SOOP_options:
                self.restricted = SOOP_options['Restricted']
            else:
                self.restricted = False

    def inital_step(self, dp):

        self.ddata = [0]
        self.xda = [self.ds[-1].x]
        self.params = self.get_params_ini(self.xda[0], npar=self.npar)

        jac = self.jac.evaluate_jac(dp.x)

        dd = self.cal_dd(jac[1], dp)
        if dd < 1e-6:
            dd = 1e-4

        return  dp.x - 0.01 * dd * jac[1]

    def general_step(self, dp):
        # Update curve fit data.
        self.xda.append(self.ds[-1].x)
        self.ddata.append(self.ddata[-1] + vecnorm(self.xda[-2] - self.xda[-1]))
        if len(self.xda) > self.nsamp:
            del self.xda[0]
            del self.ddata[0]
            self.params[:, 0] = self.xda[0]
        xdata = np.asarray(self.xda, dtype=np.float64)

        # Do curve fitting
        self.params, pord = self.do_appr(self.ddata, xdata, self.params)

        # Approximate the distance needed for the update point along the curve.
        drda = self.appdrd(self.ddata[-1], self.params, pord=pord)
        dd = self.cal_dd(drda, self.ds[-1])

        # Decrease the first step size in case of inadequate approximation.
        if len(self.ddata) < self.npar:
            dd = 0.1 * dd

        # Get x_es at approximated distance.
        return self.apprd((self.ddata[-1] + dd), self.params, pord=pord)

    def solve(self):
        LOGGER.log(logging.INFO, "%s initialise", type(self).__name__)
        self.initialize_method()

        self.ds.append(self.ds_ini[0])

        return self.run()






class Results(object):
    def __init__(self):
        pass



##############################################################################
# Tools (classes)
# functional wrappers
class FunctionWrapper(object):
    def __init__(self, funcs):
        self.funcs_ini = funcs
        self.num_sing_eva = 0
        self.num_arr_eva = 0
        self.noutp = len(funcs)

        self.x = None
        self.f = None
        self.i = None

    # returns solution fi(x)
    @cached(cache)
    def cahched_func(self, x, i):
        self.num_sing_eva += 1
        return float(self.funcs_ini[self.i](self.x))


    def evaluate_func(self, x, i, **kwargs):
        self.x = x
        self.i = i
        if isinstance(x, list):
            x = np.asarray(x)
        return self.cahched_func(hash(x.tostring()), i)

    # returns function fi
    def single_func(self, i, **kwargs):
        def func(x):
            return self.evaluate_func(x, i)

        return func

    # returns solution f(x), as array
    def evaluate_funcs(self, x, f=None, ind=None, **kwargs):
        self.num_arr_eva += 1
        if f is None:
            return np.asarray([self.evaluate_func(x, i) for i in range(self.noutp)], dtype=float)
        else:
            l = []
            for i in range(self.noutp):
                if i != ind:
                    l.append(self.evaluate_func(x, i))
                else:
                    l.append(f)
            return np.asarray(l)

    # returns function f, as array
    def array_funcs(self, **kwargs):
        def funcs(x):
            return self.evaluate_funcs(x)
        return funcs

    # returns function mu, for a specific lamb
    def combine_funcs(self, lamb, **kwargs):
        self.num_arr_eva += 1

        def objfunc(x):
            return sum(la * self.evaluate_func(x, i) for i, la in enumerate(lamb) if la != 0)

        return objfunc

    def clear(self):
        self.num_sing_eva = 0
        self.num_arr_eva = 0
        self.x = None
        self.f = None
        self.i = None
        cache.clear()

    def revers(self):
        self.funcs_ini = list(reversed(self.funcs_ini))


# constraints wrappers
class ConstraintWrapper(object):
    def __init__(self, constraints, eps=1e-8):
        if constraints is None:
            self.con_ini = []
            self.eps = eps
            self.cons = None
            self.x = None
            self.f = None
            self.fun = None
            self.ncons = 0
        else:
            # Constraints are triaged per type into a dictionnary of tuples
            self.con_ini = copy.copy(constraints)
            if isinstance(constraints, dict):
                constraints = (constraints,)

            self.cons = {'eq': (), 'ineq': ()}
            for ic, con in enumerate(constraints):
                # check type
                try:
                    ctype = con['type'].lower()
                except KeyError:
                    raise KeyError('Constraint %d has no type defined.' % ic)
                except TypeError:
                    raise TypeError('Constraints must be defined using a '
                                    'dictionary.')
                except AttributeError:
                    raise TypeError("Constraint's type must be a string.")
                else:
                    if ctype not in ['eq', 'ineq']:
                        raise ValueError("Unknown constraint type '%s'." % con['type'])

                # check function
                if 'fun' not in con:
                    raise ValueError('Constraint %d has no function defined.' % ic)

                # check jacobian
                cjac = con.get('jac')
                if cjac is None or cjac == '2-point':
                    def cjac_factory(fun):
                        def cjac(x, *args):
                            return self.grad_fw(x, fun, *args)

                        return cjac

                    cjac = cjac_factory(con['fun'])

                elif cjac == '3-point':
                    def cjac_factory(fun):
                        def cjac(x, *args):
                            return self.grad_mid(x, fun, *args)

                        return cjac

                    cjac = cjac_factory(con['fun'])

                # update constraints' dictionary
                self.cons[ctype] += ({'fun': con['fun'],
                                      'jac': cjac,
                                      'args': con.get('args', ())},)

                self.eps = eps

                self.x = None
                self.f = None
                self.fun = None

                self.ncons = len(constraints)

    # returns solution fprimei(x), 2-point
    def grad_fw(self, x, fun, *args):
        if np.all(self.x == x) and self.fun == fun:
            pass
        else:
            self.x = np.copy(x)
            self.fun = copy.copy(fun)
            self.f = copy.copy(fun(x))
        grad = np.zeros(len(x), float)
        dx = np.zeros(len(x), float)
        for j in range(len(x)):
            dx[j] = self.eps
            grad[j] = (fun(x + dx) - self.f) / self.eps
            dx[j] = 0.0
        return grad

    # returns solution fprimei(x), 3-point
    def grad_mid(self, x, fun, *args):
        if np.all(self.x == x) and self.fun == fun:
            pass
        else:
            self.x = np.copy(x)
            self.fun = copy.copy(fun)
            self.f = copy.copy(fun(x))
        grad = np.zeros(len(x), float)
        dx = np.zeros(len(x), float)
        for j in range(len(x)):
            dx[j] = self.eps
            grad[j] = (fun(x + dx) - fun(x - dx)) / (2 * self.eps)
            dx[j] = 0.0
        return grad

    # returns solution fi(x)
    def evaluate_con(self, x, i, **kwargs):
        return float(self.cons["ineq"][i]["fun"](x))

    # returns function fi
    def single_con(self, i, **kwargs):
        def con(x):
            return self.evaluate_con(x, i)

        return con

    # returns solution f(x), as array
    def evaluate_cons(self, x, f=None, ind=None, **kwargs):
        # self.num_arr_eva += 1
        if f is None:
            return np.asarray([self.evaluate_con(x, i) for i in range(self.ncons)], dtype=float)
        else:
            l = []
            for i in range(self.ncons):
                if i != ind:
                    l.append(self.evaluate_con(x, i))
                else:
                    l.append(f)
            return np.asarray(l)

    # returns function f, as array
    def array_cons(self, **kwargs):
        def cons(x):
            return self.evaluate_cons(x)

        return cons

    def evaluate_conj(self, x, i, **kwargs):
        return self.cons["ineq"][i]["jac"](x)

    def add_constraint(self, cons, **kwargs):
        for ic, con in enumerate(cons):
            cjac = con.get('jac')
            if cjac is None or cjac == '2-point':
                def cjac_factory(fun):
                    def cjac(x, *args):
                        return self.grad_fw(x, fun, *args)

                    return cjac

                cjac = cjac_factory(con['fun'])

            elif cjac == '3-point':
                def cjac_factory(fun):
                    def cjac(x, *args):
                        return self.grad_mid(x, fun, *args)

                    return cjac

                cjac = cjac_factory(con['fun'])

            con['jac'] = cjac

        return self.con_ini + cons


# limits wrappers
class LimitWrapper(object):
    def __init__(self, limits, n_input):
        if limits is None:
            self.lims_ini = None
        else:
            self.lims_ini = limits
        self.lob, self.upb = self.get_limits(limits, n_input)

    def get_limits(self, bounds, n_input):
        if bounds is None or len(bounds) == 0:
            return np.array([-1.0E12] * n_input), np.array([1.0E12] * n_input)
        else:
            bnds = np.array(bounds, float)
            if bnds.shape[0] != n_input:
                raise IndexError('Error: the length of bounds is not'
                                 'compatible with that of x0.')

            bnderr = np.where(bnds[:, 0] > bnds[:, 1])[0]
            if bnderr.any():
                raise ValueError('Error: lb > ub in bounds %s.' %
                                 ', '.join(str(b) for b in bnderr))
            return bnds[:, 0], bnds[:, 1]


# jacobian wrappers
class JacobianWrapper(object):
    def __init__(self, funcs, jac, eps=1e-8):
        if jac is None:
            self.jac_ini = None
        else:
            self.jac_ini = copy.copy(jac)
        self.funcs = funcs
        self.noutp = len(funcs)

        self.jac = []
        if jac == '2-point':
            self.jac = [self.gradi_fw(i) for i in range(self.noutp)]
        elif jac == '3-point':
            self.jac = [self.gradi_mid(i) for i in range(self.noutp)]
        elif isinstance(jac, (list,)):
            for i, grad in enumerate(jac):
                if callable(grad):
                    self.jac.append(grad)
                elif grad == '2-point' or grad is None:
                    self.jac.append(self.gradi_fw(i))
                elif grad == '3-point':
                    self.jac.append(self.gradi_mid(i))
                else:
                    # warn('Gradient %i is not correct, 2-point is used.' % i)
                    self.jac.append(self.gradi_fw(i))
        else:
            # warn('Jacobian is not correct, 2-point is used.')
            self.jac = [self.gradi_fw(i) for i in range(self.noutp)]

        self.num_jac_eva = 0
        self.num_grad_eva = 0
        self.num_sing_eva = 0

        self.eps = eps

        self.x = None
        self.f = None
        self.i = None

    # returns solution fi(x)
    @cached(cache2)
    def cahched_func(self, x, i):
        self.num_sing_eva += 1
        return float(self.funcs[self.i](self.x))


    def evaluate_func(self, x, i, **kwargs):
        self.x = x
        self.i = i
        if isinstance(x, list):
            x = np.asarray(x)
        return self.cahched_func(hash(x.tostring()), i)

    # returns solution fprimei(x), callable
    def evaluate_grad(self, x, i):
        self.num_grad_eva += 1
        return np.asarray(self.jac[i](x), dtype=float)

    # returns function fprimei, callable
    def single_grad(self, i):
        def func(x):
            return self.evaluate_grad(x, i)

        return func

    # returns solution fprimei(x), callable
    def evaluate_grad_neg(self, x, i):
        self.num_grad_eva += 1
        return np.asarray(-self.jac[i](x), dtype=float)

    # returns function fprimei, callable
    def single_grad_neg(self, i):
        def func(x):
            return self.evaluate_grad_neg(x, i)

        return func

    # returns solution fprimei(x), 2-point
    def grad_fw(self, x, i):
        if np.all(self.x == x) and self.i == i:
            pass
        else:
            self.x = np.copy(x)
            self.i = copy.copy(i)
            self.f = copy.copy(self.evaluate_func(x, i))
        grad = np.zeros(len(x), float)
        dx = np.zeros(len(x), float)
        for j in range(len(x)):
            dx[j] = self.eps
            grad[j] = (self.evaluate_func((x + dx), i) - self.f) / self.eps
            dx[j] = 0.0
        return grad

    # returns solution fprimei(x), 3-point
    def grad_mid(self, x, i):
        grad = np.zeros(len(x), float)
        dx = np.zeros(len(x), float)
        for j in range(len(x)):
            dx[j] = self.eps
            grad[j] = (self.evaluate_func((x + dx), i) - self.evaluate_func((x - dx), i)) / (2 * self.eps)
            dx[j] = 0.0
        return grad

    # returns function fprimei, callable 2-point
    def gradi_fw(self, i):
        def func(x):
            return self.grad_fw(x, i)

        return func

    # returns function fprimei, callable 3-point
    def gradi_mid(self, i):
        def func(x):
            return self.grad_mid(x, i)

        return func

    # returns solution jac(x)
    def evaluate_jac(self, x, grad=None, ind=None, **kwargs):
        jac = np.zeros((len(self.funcs), len(x)))
        for i in range(self.noutp):
            if i == ind and grad is not None:
                jac[i] = grad
            else:
                jac[i] = self.evaluate_grad(x, i)
        return jac

    # returns function mu, for a specific lamb
    def combine_grad(self, lamb, **kwargs):
        def objfunc(x):
            return np.sum(la * self.evaluate_grad(x, i) for i, la in enumerate(lamb) if la != 0)

        return objfunc

    # update jac for non-smooth
    def update_jac(self, jac, **kwargs):
        self.jac = []
        if jac == '2-point':
            self.jac = [self.gradi_fw(i) for i in range(self.noutp)]
        elif jac == '3-point':
            self.jac = [self.gradi_mid(i) for i in range(self.noutp)]
        elif isinstance(jac, (list,)):
            for i, grad in enumerate(jac):
                if callable(grad):
                    self.jac.append(grad)
                elif grad == '2-point' or grad is None:
                    self.jac.append(self.gradi_fw(i))
                elif grad == '3-point':
                    self.jac.append(self.gradi_mid(i))
                else:
                    # warn('Gradient %i is not correct, 2-point is used.' % i)
                    self.jac.append(self.gradi_fw(i))
        else:
            # warn('Jacobian is not correct, 2-point is used.')
            self.jac = [self.gradi_fw(i) for i in range(self.noutp)]

    def clear(self):
        self.num_jac_eva = 0
        self.num_grad_eva = 0
        self.num_sing_eva = 0
        self.x = None
        self.f = None
        self.i = None
        cache2.clear()

    def revers(self):
        self.funcs = list(reversed(self.funcs))


##############################################################################
# Termination conditions
class TerminationCondition(object):
    """Abstract class for defining termination conditions."""

    __metaclass__ = ABCMeta

    def __init__(self):
        super(TerminationCondition, self).__init__()

    def __call__(self, problem):
        return self.shouldTerminate(problem)

    def initialize(self, problem):
        """Initializes this termination condition.

        This method is used to collect any initial state, such as the current
        NFE or current time, needed for calculating the termination criteria.

        Parameters
        ----------
        problem : Algorithm
            The algorithm being run.
        """
        pass

    @abstractmethod
    def shouldTerminate(self, problem):
        """Checks if the algorithm should terminate.

        Check the termination condition, returning True if the termination
        condition is satisfied; False otherwise.  This method is called after
        each iteration of the algorithm.

        Parameters
        ----------
        problem : Algorithm
            The algorithm being run.
        """
        raise NotImplementedError("method not implemented")


class MaxEvaluations(TerminationCondition):
    """Termination condition based on the maximum number of function evaluations.

    Note that since we check the termination condition after each iteration, it
    is possible for the algorithm to exceed the max NFE.

    Parameters
    ----------
    nfe : int
        The maximum number of function evaluations to execute.
    """

    def __init__(self, maxnfe):
        super(MaxEvaluations, self).__init__()
        self.maxnfe = maxnfe
        self.starting_nfe = 0

    def initialize(self, problem):
        self.starting_nfe = problem.funcs.num_sing_eva

    def shouldTerminate(self, problem):
        if problem.funcs.num_sing_eva - self.starting_nfe >= self.maxnfe:
            print(f"{type(problem).__name__} finished due to reaching max evalutions: {self.maxnfe}.")
            return True
        else:
            return False


class MaxTime(TerminationCondition):
    """Termination condition based on the maximum elapsed time."""

    def __init__(self, max_time):
        super(MaxTime, self).__init__()
        self.max_time = max_time
        self.start_time = time.time()

    def initialize(self, problem):
        self.start_time = time.time()

    def shouldTerminate(self, problem):
        if time.time() - self.start_time >= self.max_time:
            print(f"{type(problem).__name__} finished due to reaching max time: {self.max_time}.")
            return True
        else:
            return False


class ParetoPoint(dict):
    """ Represents the optimization result.

    Attributes
    ----------
    x : ndarray
        The solution of the optimization.
    success : bool
        Whether or not the optimizer exited successfully.
    status : int
        Termination status of the optimizer. Its value depends on the
        underlying solver. Refer to `message` for details.
    message : str
        Description of the cause of the termination.
    fun, jac, hess: ndarray
        Values of objective function, its Jacobian and its Hessian (if
        available). The Hessians may be approximations, see the documentation
        of the function in question.
    hess_inv : object
        Inverse of the objective function's Hessian; may be an approximation.
        Not available for all solvers. The type of this attribute may be
        either np.ndarray or scipy.sparse.linalg.LinearOperator.
    nfev, njev, nhev : int
        Number of evaluations of the objective functions and of its
        Jacobian and Hessian.
    nit : int
        Number of iterations performed by the optimizer.
    maxcv : float
        The maximum constraint violation.

    Notes
    -----
    There may be additional attributes not listed above depending of the
    specific solver. Since this class is essentially a subclass of dict
    with attribute accessors, one can see which attributes are available
    using the `keys()` method.
    """
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)

    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def __repr__(self):
        if self.keys():
            m = max(map(len, list(self.keys()))) + 1
            return '\n'.join([k.rjust(m) + ': ' + repr(v)
                              for k, v in sorted(self.items())])
        else:
            return self.__class__.__name__ + "()"

    def __dir__(self):
        return list(self.keys())

##############################################################################
# Evaluation
def Eveness(ds):

    ds = sorted(ds, key=lambda x: x.f[0], reverse=False)

    d = []
    for i, dpi in enumerate(ds):
        if i != 0:
            d.append(vecnorm(dpi.f - ds[i - 1].f))

    sum = 0
    for di in d:
        sum += di
    mu = sum/len(d)

    sum2 = 0
    for i, di in enumerate(d):
        if i != 0:
            sum2 += (di - mu) ** 2

    si = np.sqrt(sum2 / (len(d) - 1))

    # return si / mu

    ol = mu - si
    i = 0
    while i < len(d)-1:
        if d[i] < ol:
            d[i+1] += d[i]
            del d[i]
        else:
            i += 1

    mu = sum / len(d)

    sum2 = 0
    for i, di in enumerate(d):
        if i != 0:
            sum2 += (di - mu) ** 2
            sum2 += (d[i-1] - mu) ** 2

    si = np.sqrt(sum2 / (2*len(d) - 1))

    return si / mu



