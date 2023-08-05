import numpy as np
import scipy as sp
from numpy import ndarray
from stft import ispectrogram, spectrogram


def solve_in(domain: str):
    def _solve_in(func):
        def wrapper(d: ndarray, x: ndarray, w: ndarray, mu: float, _):
            if domain == "freq":
                d = spectrogram(d)
                x = spectrogram(x)
            w_delta = func(d, x, w, mu, _)[:]
            if domain == "freq":
                return ispectrogram(w_delta)[:]
            else:
                return w_delta[:]

        return wrapper

    return _solve_in


def lms(d: ndarray, x: ndarray, w: ndarray, mu: float, _):
    """
    Least-Mean-Square filtering.
    """
    N = d.shape

    y = np.zeros_like(d)
    e = np.zeros_like(d)

    djdw = np.zeros_like(w)
    w_delta = np.zeros_like(w)

    for k in range(N):
        y[k] = np.dot(w, x[k])
        e[k] = d[k] - y[k]
        # 2 * J = e ** 2
        djdw[k] = e[k] * x[k]

    w_delta = mu * djdw[:]
    return w_delta[:]


def nlms(d: ndarray, x: ndarray, w: ndarray, mu: float, lambda_: float = 1.0):
    N = d.shape

    y = np.zeros_like(d)
    e = np.zeros_like(d)

    djdw = np.zeros_like(w)
    w_delta = np.zeros_like(w)

    for k in range(N):
        y[k] = np.dot(w, x[k])
        e[k] = d[k] - y[k]
        # 2 * J = e ** 2 - sum(w[i] ** 2 for i in range(N))
        djdw[k] = e[k] * x[k]

    w_delta = mu / (np.dot(x.T, x) + lambda_) * djdw[:]
    return w_delta[:]
