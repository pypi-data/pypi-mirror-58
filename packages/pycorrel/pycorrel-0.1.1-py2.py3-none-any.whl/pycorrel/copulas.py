
import abc
import numpy as np
import scipy.stats as sps

class Copula(abc.ABC):
    """Abstract base class for copulas.
    """

    @abc.abstractmethod
    def draw(self, size):
        """Draws a sample from the copula.

            Variables always span along the first axis.

        Parameters
        ----------
        size : int or tuple of ints
            The size of the sample to draw.

        Returns
        -------
        ndarray
            The sample drawn for the copula.
        """
        pass

    @abc.abstractproperty
    def dimension(self):
        """int : The underlying dimension of the copula.
        """
        pass

class GaussianCopula(Copula):

    def __init__(self, correlation_matrix):
        """Gaussian copula with given correlation matrix.

        Parameters
        ----------
        correlation_matrix : ndarray (square matrix)
            The correlation matrix of the gaussian copula.
            The size of the matrix corresponds to the dimension of the copula.
        """
        U, s, _ = np.linalg.svd(correlation_matrix)
        self.A = U * np.sqrt(s)
        self.d, _ = correlation_matrix.shape

    def draw(self, size):
        if type(size) is int:
            size = (size,)
        z = np.random.normal(size = (self.d,) + size)
        return sps.norm.cdf(np.tensordot(self.A, z, 1))

    @property
    def dimension(self):
        return self.d
