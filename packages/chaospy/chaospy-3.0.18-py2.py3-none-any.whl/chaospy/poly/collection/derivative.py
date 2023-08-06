"""
Polynomial transformation functions involving derivatives.
"""

import numpy as np
from scipy.special import factorial

import chaospy.poly.caller
import chaospy.poly.collection
import chaospy.poly.dimension

from chaospy.poly import Poly


def differential(poly, diffvar):
    """
    Polynomial differential operator.

    Args:
        poly (Poly) : Polynomial to be differentiated.
        diffvar (Poly) : Polynomial to differentiate by. Must be decomposed. If
                polynomial array, the output is the Jacobian matrix.

    Examples:
        >>> q0, q1 = chaospy.variable(2)
        >>> poly = chaospy.Poly([1, q0, q0*q1**2+1])
        >>> print(poly)
        [1, q0, q0q1^2+1]
        >>> print(differential(poly, q0))
        [0, 1, q1^2]
        >>> print(differential(poly, q1))
        [0, 0, 2q0q1]
    """
    poly = Poly(poly)
    diffvar = Poly(diffvar)

    if not chaospy.poly.caller.is_decomposed(diffvar):
        sum(differential(poly, chaospy.poly.caller.decompose(diffvar)))

    if diffvar.shape:
        return Poly([differential(poly, pol) for pol in diffvar])

    if diffvar.dim > poly.dim:
        poly = chaospy.poly.dimension.setdim(poly, diffvar.dim)
    else:
        diffvar = chaospy.poly.dimension.setdim(diffvar, poly.dim)

    qkey = diffvar.keys[0]

    core = {}
    for key in poly.keys:

        newkey = np.array(key) - np.array(qkey)

        if np.any(newkey < 0):
            continue
        newkey = tuple(newkey)
        core[newkey] = poly.A[key] * np.prod(
            [factorial(key[idx], exact=True) / factorial(newkey[idx], exact=True)
             for idx in range(poly.dim)])

    return Poly(core, poly.dim, poly.shape, poly.dtype)


def gradient(poly):
    """
    Gradient of a polynomial.

    Args:
        poly (Poly) : polynomial to take gradient of.

    Returns:
        (Poly) : The resulting gradient.

    Examples:
        >>> q0, q1, q2 = chaospy.variable(3)
        >>> poly = 2*q0 + q1*q2
        >>> print(chaospy.gradient(poly))
        [2, q2, q1]
    """
    return differential(
        poly, chaospy.poly.collection.basis(1, 1, poly.dim, sort="GR"))


def hessian(poly):
    """
    Make Hessian matrix out of a polynomial.

    Args:
        poly (Poly) : polynomial to take Hessian of.

    Returns:
        (Poly) : The resulting Hessian.

    Examples:
        >>> q0, q1, q2 = chaospy.variable(3)
        >>> poly = 2*q0**2 + q1**2*q2
        >>> print(chaospy.hessian(poly))
        [[4, 0, 0], [0, 2q2, 2q1], [0, 2q1, 0]]
    """
    return gradient(gradient(poly))
