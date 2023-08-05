import numpy as np


def lms(d: np.ndarray, x: np.ndarray, w: np.ndarray, mu: float, _):
    """
    Least-Mean-Square filtering.
    """
    N = d.shape[0]

    y = np.zeros_like(d)
    e = np.zeros_like(d)

    djdw = np.zeros_like(w)
    w_delta = np.zeros_like(w)

    for k in range(N):
        y[k] = np.dot(w, x)
        e[k] = d[k] - y[k]
        # 2 * J = e ** 2
        djdw[k] = x[k] * e[k]

    w_delta = mu * djdw
    return w_delta


def nlms(d: np.ndarray, x: np.ndarray, w: np.ndarray, mu: float, lambda_: float = 1.0):
    N = d.shape[0]

    y = np.zeros_like(d)
    e = np.zeros_like(d)

    djdw = np.zeros_like(w)
    w_delta = np.zeros_like(w)

    for k in range(N):
        y[k] = np.dot(w, x)
        e[k] = d[k] - y[k]
        # 2 * J = e ** 2 - sum(w[i] ** 2 for i in range(N))
        djdw[k] = x[k] * e[k]

    w_delta = mu / (np.dot(x.T, x) + lambda_) * djdw
    return w_delta
