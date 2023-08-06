# -*- coding: utf-8 -*-

"""
forrester.py: Forrester function

This file contains the definition of an adapted version of the simple 1D
example function as presented in the paper(s) by Forrester et al.

This version has been adapted in the following ways:
 - Inverted, the optimum is a maximum, not a minimum
 - Translated, the (1D) output values have been translated upwards to always
   be positive, i.e. [~0, ~22]
 - Multi-dimensional, input can be arbitrarily many dimensions. Output value
   is calculated as the weighted sum of each separable dimension.
"""

import numpy as np

from .multiFidelityFunction import MultiFidelityFunction


l_bound = [0]
u_bound = [1]

def forrester_high(X):
    X = np.atleast_2d(X)

    ndim = X.shape[1]
    term1 = (6*X - 2)**2
    term2 = np.sin(12*X - 4)
    return np.sum(term1 * term2, axis=1) / ndim


def forrester_low(X):
    X = np.atleast_2d(X)

    ndim = X.shape[1]
    term1 = 0.5*forrester_high(X)
    term2 = 10*(X - 0.5) - 5

    return term1 - (np.sum(term2, axis=1) / ndim)


def Forrester(ndim=1):
    if not isinstance(ndim, int):
        raise TypeError(f"ndim must be of type 'int', not {type(ndim)}")
    if ndim < 1:
        raise ValueError(f"ndim must be at least 1, not {ndim}")

    return MultiFidelityFunction(
        "forrester",
        u_bound=np.repeat(u_bound, ndim),
        l_bound=np.repeat(l_bound, ndim),
        functions=[forrester_high, forrester_low],
        fidelity_names=['high', 'low'],
    )


forrester = Forrester(ndim=1)


forrester_sf = MultiFidelityFunction(
    "forrester single fidelity",
    u_bound=u_bound, l_bound=l_bound,
    functions=[forrester_high],
    fidelity_names=['high'],
)
