import numpy as np
from nptyping import Array


def lms(d: Array, x: Array, w: Array, mu: float, _) -> Array:
    """
    lms Least-Mean-Square filtering.
    
    Args:
        d (Array): Desired values.
        x (Array): Input(recorded) values.
        w (Array): Filter-weight matrix.
        mu (float): Step size.
        _ ([dummy argument]): DO NOT SET ANY VALUE.
    
    Returns:
        Array: Modified value array of w.
    """
    N = d.shape[0]

    y = np.zeros_like(d)
    e = np.zeros_like(d)

    # diff_J_for_w: 誤差パワーJ ( J ＝ 1/2 * e^2 , 誤差信号 e の二次関数) を w で微分した値
    # w_delta: 係数行列wの更新量
    diff_J_for_w = np.zeros_like(w)
    w_delta = np.zeros_like(w)

    for k in range(N):
        y[k] = w[k] * x[k]
        e[k] = d[k] - y[k]
        # 2 * J = e ** 2
        diff_J_for_w[k] = x[k] * e[k]

    w_delta = mu * diff_J_for_w
    return w_delta


def nlms(d: Array, x: Array, w: Array, mu: float, lambda_: float = 1.0) -> Array:
    """
    Normalized-LMS filtering.

    Args:
        d (Array): Desired values.
        x (Array): Input(recorded) values.
        w (Array): Filter-weight matrix.
        mu (float): Step size.
        lambda_ (float, optional): Learning rate. Defaults to 1.0.

    Returns:
        Array: Modified value array of w.
    """

    N = d.shape[0]

    y = np.zeros_like(d)
    e = np.zeros_like(d)

    # diff_J_for_w: 誤差パワーJ ( J ＝ 1/2 * e^2 , 誤差信号 e の二次関数) を w で微分した値
    # w_delta: 係数行列wの更新量
    diff_J_for_w = np.zeros_like(w)
    w_delta = np.zeros_like(w)

    for k in range(N):
        y[k] = w[k] * x[k]
        e[k] = d[k] - y[k]
        # 2 * J = e ** 2 - sum(w[i] ** 2 for i in range(N))
        diff_J_for_w[k] = x[k] * e[k]
        w_delta[k] = mu / (np.abs(x[k]) ** 2 + lambda_) * diff_J_for_w[k]

    return w_delta
