import numpy as np

def reorder(a, ranks, axis=-1):
    """Reorders an array according to given ranks.

    Parameters
    ----------
    a : array_like
        Array to reorder.
    ranks : array_like
        Array of ranks (`int`) used to reorder the array.
        This array should have the same shape as `a`.
    axis : int, optional
        Axis along which to reorder. The default is -1 (the last axis).

    Returns
    -------
    ndarray
        The reordered array.
    """
    return np.take_along_axis(np.sort(a, axis=axis), ranks, axis=axis)

def rankdata(a, axis=-1):
    """Assigns ranks to each element of `a` sorting along the specified `axis`.

        Contrary to the homonymous function in SciPy , ranks are always
        integer-valued. Ties are handled in an arbitrary way.

    Parameters
    ----------
    a : array_like
        The array of values to be ranked.
    axis : int, optional
        Axis along which to sort. The default is -1 (the last axis).

    Returns
    -------
    ndarray
        An array of `int` of the same shape as `a` containing the ranks of
        each of its elements.
    """
    shape = a.shape
    if axis == -1:
        axis = len(shape) - 1

    tmp_1 = (1,) * axis + (shape[axis],) + (1,) * (len(shape) - axis - 1)
    tmp_2 = shape[:axis] + (1,) + shape[axis+1:]
    orders = a.argsort(axis=axis)
    ranks = np.empty_like(orders)
    np.put_along_axis(ranks, orders,
        np.tile(np.arange(shape[axis]).reshape(tmp_1), tmp_2), axis=axis)
    return ranks

def covariances(a, sampling_axis=0, variables_axis=1):
    """Estimates covariance matrices from the given data.

    Parameters
    ----------
    a : array_like
        A `M`-D array (`M` > 1) containing multiple observations
        (along axis `sampling_axis`) and variables
        (along axis `variables_axis`).
        Additional axes may be used to allow for several batches of data.
    sampling_axis : int, optional
        The axis along which observations are stored, by default 0.
    variables_axis : int, optional
        The axis along which variables span, by default 1.

    Returns
    -------
    ndarray
        A `M`-D array whose first axes correspond to the additional axes and
        whose two last axes corresponds to the estimated covariance matrices.
    """
    n = a.shape[sampling_axis]
    means = a.mean(axis=sampling_axis)
    tmp = a - np.expand_dims(means, sampling_axis)
    tmp = np.moveaxis(tmp, [variables_axis, sampling_axis], [0, 1])
    return np.einsum('ij...,kj...->...ik', tmp, tmp) / (n - 1)

def correlations(a, sampling_axis=0, variables_axis=1):
    """Estimates correlation matrices from the given data.

    Parameters
    ----------
    a : array_like
        A `M`-D array (`M` > 1) containing multiple observations
        (along axis `sampling_axis`)
        and variables (along axis `variables_axis`).
        Additional axes may be used to allow for several batches of data.
    sampling_axis : int, optional
        The axis along which observations are stored, by default 0.
    variables_axis : int, optional
        The axis along which variables span, by default 1.

    Returns
    -------
    ndarray
        A `M`-D array whose first axes correspond to the additional axes and
        whose two last axes corresponds to the estimated correlation matrices.
    """
    covariances_ = covariances(a, sampling_axis, variables_axis)
    variances = np.einsum('...ii->...i', covariances_)
    return covariances_ / np.sqrt(np.einsum('...i,...j', variances, variances))
