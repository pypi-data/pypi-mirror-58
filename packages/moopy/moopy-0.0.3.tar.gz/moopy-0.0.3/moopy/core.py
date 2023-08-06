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


class PSE(object):
    def __init__(self):
        self.funcs = None
        self.limits = None
        self.constraints = None
        self.jac = None
        self.finished = False

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
        for i in range(self.ninp):
            params[i, :npar], pcov = self.do_curve_fit(ddata, xdata[:, i], params[i, :], pord=pord)

        return params, pord

    ###########################################################################################
    # Functionals
    def method_info(self):
        if self.prt_info:
            print('Number of single function evaluations:', self.funcs.num_sing_eva)
            print('Number of Jacobian evaluations:', self.jac.num_grad_eva)
            print('Number of iterations:', self.it)
            print('Number of Pareto points:', len(self.ds))

        return [self.funcs.num_sing_eva, self.jac.num_grad_eva, self.it, len(self.ds)]

    def get_dp(self, x):
        return OptimizeResult(f=self.funcs.evaluate_funcs(x), x=x, g = self.constraints.evaluate_cons(x))

    def get_act_bounds(self, dp):
        return list(dp.x <= self.limits.lob + self.tol) + \
               list(dp.x >= self.limits.upb - self.tol) + \
               list(dp.g <= 0 + self.tol)

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

        con = [{'type': 'ineq', 'fun': lambda x: dp.f[0] - self.funcs.single_func(0)(x),}]
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

    def finish_PSE2(self, dp):
        # self.ds.append(dp)
        # self.ds.append(self.ds_ini[1])
        return self.ds, self.method_info()

    ###########################################################################################
    # PSE initialization
    def solve(self, funs, ds_ini, lims, cons, jac, options, *args, **kwargs):

        self.ninp = len(ds_ini[0][0])
        if not isinstance(funs, FunctionWrapper):
            self.funcs = FunctionWrapper(funs)
        else:
            self.funcs = funs
        if not isinstance(lims, LimitWrapper):
            self.limits = LimitWrapper(lims, self.ninp)
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

        # self.ds_ini = []
        # for xi in ds_ini:
        #     self.ds_ini.append(self.get_dp(xi[0]))

        if options is None:
            self.options = {}
        else:
            self.options = dict(options)

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

        self.d1 = self.options.pop('d1', 0.01)
        self.d2 = self.options.pop('d2', 0.01)

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


        # dp0 = self.get_dp(x_ini)
        dp0 = self.get_dp(ds_ini[0][0])


        return self.__PSE(dp0)

    ###########################################################################################
    # PSE method
    def __PSE(self, dp):

        self.ds = []
        self.ds.append(dp)
        self.it = 1

        while not self.finished:
            if self.it == 1:

                ddata = [0]
                xda = [dp.x]
                params = self.get_params_ini(dp.x, npar=self.npar)

                jac = self.jac.evaluate_jac(dp.x)

                x_es = dp.x - self.d1 * (jac[1]/vecnorm(jac[1]))

                if self.prt_steps:
                    print(self.it)
                    print(dp.x - (jac[1] / vecnorm(jac[1])))
                    print(x_es)

            else:
                # Update curve fit data.
                xda.append(self.ds[-1].x)
                ddata.append(ddata[-1] + vecnorm(xda[-2] - xda[-1]))
                if len(xda) > self.nsamp:
                    del xda[0]
                    del ddata[0]
                    params[:, 0] = xda[0]
                xdata = np.asarray(xda, dtype=np.float64)

                # Do curve fitting
                params, pord = self.do_appr(ddata, xdata, params)

                # Decrease the first step size in case of inadequate approximation.
                if len(ddata) < self.npar:
                    dd = 0.1*self.d2
                else:
                    dd = self.d2

                # Get x_es at approximated distance.
                x_es = self.apprd((ddata[-1] + dd), params, pord=pord)

                if self.prt_steps:
                    print(self.it)
                    print(ddata)
                    print(xdata)
                    print(params)
                    print(x_es)

            # Define and solve SOOP
            x_es = self.check_x(x_es)
            dp = self.perform_SOOP(x_es)

            if self.check_finished(dp):
                return self.finish_PSE2(dp)

            elif self.check_nonsmooth(dp):
                self.it = 1
                self.ds.append(dp)
            else:
                self.ds.append(dp)

                # Iteration count and check for infinite loops
                self.it += 1
                if self.it > 300:
                    self.finished = True

        return self.ds, self.method_info()


class NC(object):
    def __init__(self):
        self.funcs = None
        self.limits = None
        self.constraints = None
        self.jac = None
        self.finished = False

    ###########################################################################################
    # Functionals
    def method_info(self):
        if self.prt_info:
            print('Number of single function evaluations:', self.funcs.num_sing_eva)
            print('Number of Jacobian evaluations:', self.jac.num_grad_eva)
            print('Number of iterations:', self.it)
            print('Number of Pareto points:', len(self.ds))

        return [self.funcs.num_sing_eva, self.jac.num_grad_eva, self.it, len(self.ds)]


    def get_dp(self, x):
        return OptimizeResult(f=self.funcs.evaluate_funcs(x), x=x, g = self.constraints.evaluate_cons(x))

    ###########################################################################################
    # SOOP function
    def perform_SOOP_NC(self, dp):

        con = [{'type': 'ineq', 'fun': lambda x: -np.dot(self.v[0], (self.funcs.evaluate_funcs(x) - self.p[self.it]))}]
        if self.jac.jac_ini == '2-point' or self.jac.jac_ini == '3-point':
            con[0]['jac'] = self.jac.jac_ini
        cons = self.constraints.add_constraint(con)

        res = minimize(self.funcs.single_func(1), dp.x, bounds=self.limits.lims_ini,
                       constraints=cons, )

        # jac = self.jac.single_grad(1)

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

    ###########################################################################################
    # NC initialization
    def solve(self, funs, ds_ini, lims, cons, jac, options, *args, **kwargs):

        self.ninp = len(ds_ini[0][0])
        if not isinstance(funs, FunctionWrapper):
            self.funcs = FunctionWrapper(funs)
        else:
            self.funcs = funs
        if not isinstance(lims, LimitWrapper):
            self.limits = LimitWrapper(lims, self.ninp)
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

        self.Npar = int(self.options.pop('delta', 20))
        self.tol = self.options.pop('tol', 1e-6)
        self.prt_info = self.options.get('print_info', False)

        self.ds_ini = []
        for xi in ds_ini:
            self.ds_ini.append(self.get_dp(xi[0]))

        self.v = []
        for i, dp in enumerate(self.ds_ini):
            if i != 1:
                self.v.append(self.ds_ini[1].f - dp.f)

        self.delta = 1/self.Npar
        a1 = 1.
        a2 = 0.
        self.p = []
        for i in range(self.Npar):
            self.p.append(a1 * self.ds_ini[0].f + a2 * self.ds_ini[1].f)
            a1 -= self.delta
            a2 += self.delta

        dp0 = self.ds_ini[0]
        self.ds = []
        self.it = 1

        return self.__NC(dp0)

    ###########################################################################################
    # PSE method
    def __NC(self, dp):

        self.ds.append(dp)

        # Main iteration process
        # While the section is not finished additional points should be added to data set.
        while not self.finished:

            # Define and solve SOOP
            dp_es = self.perform_SOOP_NC(self.ds[-1])

            # Add point to data set
            self.ds.append(dp_es)

            # Iteration count and check for infinite loops
            self.it += 1
            if self.it == self.Npar:
                self.finished = True
                self.ds.append(self.ds_ini[-1])

        return self.ds, self.method_info()


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



