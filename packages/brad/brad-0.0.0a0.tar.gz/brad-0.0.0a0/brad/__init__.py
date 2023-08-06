import numpy as np
from numpy.core.numeric import asanyarray

from ._version import __version__  # noqa

__all__ = ["bootstrap"]


def bootstrap(x, n_samples, axis=0, f=None):
    """
    Generate bootstrap samples from x.

    Parameters
    ----------
    x: array_like
        Input data from which to draw bootstrap samples.
    n_samples: int
        The number of samples to draw.
    axis: int, optional
        The axis along which samples should drawn from x. Samples will be
        returned along this axis. Default: 0.
    f: callable, optional
        A function to apply to each bootstrap sample. If f is supplied then
        the returned array will have shape (n_samples, ) + f_return_shape.

    Returns
    -------
    numpy.ndarray
        An array of samples.
    """
    x = np.moveaxis(asanyarray(x), axis, 0)
    sample = x[np.random.choice(x.shape[0], n_samples), ...]

    if f is not None:
        res = asanyarray(f(sample[0]))
        buff = np.zeros((sample.shape[0],) + res.shape)

        buff[0] = res
        for i in range(1, sample.shape[0]):
            buff[i] = asanyarray(f(sample[i]))

        return buff

    return np.moveaxis(sample, 0, axis)
