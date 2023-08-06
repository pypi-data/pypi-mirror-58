"""Main module."""

import numpy as np

import pycorrel.utils


def iman_conover(sample, copula, sampling_axis=0, variables_axis=1):
    """Correlates a given sample using the Iman-Conover method.

        The Iman-Conover methods enables to reorder a sample
        to incorporate the dependency structure from a given copula.

    Parameters
    ----------
    sample : ndarray
        The sample to correlate.
    copula : pycorrel.copulas.Copula
        The copula used to correlate the sample.
    sampling_axis : int, optional
        The axis along which to reorder the sample, by default 0.
    variables_axis : int, optional
        The axis along which variables span, by default 1.

    Returns
    -------
    ndarray
        The reordered sample.
    """
    if copula.dimension != sample.shape[variables_axis]:
        raise ValueError("Dimension mismatch between sample and copula.")

    copula_sample = copula.draw(sample.shape[:variables_axis] +
        sample.shape[variables_axis + 1:])
    copula_sample = np.moveaxis(copula_sample, 0, variables_axis)
    copula_ranks = pycorrel.utils.rankdata(sample, sampling_axis)
    return pycorrel.utils.reorder(sample, copula_ranks, sampling_axis)
