"""
Identify first argument passed to class Poly constructor.
"""
import numpy

import chaospy.poly.base
import chaospy.poly.dimension
import chaospy.poly.typing


def identify_core(core):
    """Identify the polynomial argument."""
    for datatype, identifier in {
            int: _identify_scaler,
            numpy.int8: _identify_scaler,
            numpy.int16: _identify_scaler,
            numpy.int32: _identify_scaler,
            numpy.int64: _identify_scaler,
            float: _identify_scaler,
            numpy.float16: _identify_scaler,
            numpy.float32: _identify_scaler,
            numpy.float64: _identify_scaler,
            chaospy.poly.base.Poly: _identify_poly,
            dict: _identify_dict,
            numpy.ndarray: _identify_iterable,
            list: _identify_iterable,
            tuple: _identify_iterable,
    }.items():
        if isinstance(core, datatype):
            return identifier(core)

    raise TypeError(
        "Poly arg: 'core' is not a valid type " + repr(core))


def _identify_scaler(core):
    """Specification for a scaler value."""
    return {(0,): numpy.asarray(core)}, 1, (), type(core)


def _identify_poly(core):
    """Specification for a polynomial."""
    return core.A, core.dim, core.shape, core.dtype


def _identify_dict(core):
    """Specification for a dictionary."""
    if not core:
        return {}, 1, (), int

    core = core.copy()
    key = sorted(core.keys(), key=chaospy.poly.base.sort_key)[0]
    shape = numpy.array(core[key]).shape
    dtype = numpy.array(core[key]).dtype
    dim = len(key)
    return core, dim, shape, dtype


def _identify_iterable(core):
    """Specification for a list, tuple, numpy.ndarray."""
    if isinstance(core, numpy.ndarray) and not core.shape:
        return {(0,):core}, 1, (), core.dtype

    core = [chaospy.poly.base.Poly(a) for a in core]
    shape = (len(core),) + core[0].shape

    dtype = chaospy.poly.typing.dtyping(*[_.dtype for _ in core])

    dims = numpy.array([a.dim for a in core])
    dim = numpy.max(dims)
    if dim != numpy.min(dims):
        core = [chaospy.poly.dimension.setdim(a, dim) for a in core]

    out = {}
    for idx, core_ in enumerate(core):

        for key in core_.keys:

            if not key in out:
                out[key] = numpy.zeros(shape, dtype=dtype)
            out[key][idx] = core_.A[key]

    return out, dim, shape, dtype
