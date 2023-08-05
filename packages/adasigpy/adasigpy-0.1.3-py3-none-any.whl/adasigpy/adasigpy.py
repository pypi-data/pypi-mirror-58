import numpy as np

from .domain.method import Method, init_w
from .interface.filter import AdaptiveSignalProcesserABC
from .method import solve_in


class AdaptiveSignalProcesser(AdaptiveSignalProcesserABC):
    def __init__(self, model, n, mu, w, domain, lambda_):
        self.method = solve_in(domain)(Method.methods[model])
        self.n = n
        self.mu = mu
        self.w = init_w(w, n)
        self.lambda_ = lambda_

    def adopt(self, d, x):
        if d.shape[0] != x.shape[0]:
            raise ValueError(
                f"2 arrays should have same length. But now, 'd.shape'  is {d.shape} and 'x.shape' is {x.shape[0]}."
            )
        self.method(d, x, self.w, self.mu, self.lambda_)

    def apply(self, d, x):
        if d.shape[0] != x.shape[0]:
            raise ValueError(
                f"2 arrays should have same length. But now, 'd.shape'  is {d.shape} and 'x.shape' is {x.shape[0]}."
            )
        w_delta = self.method(d, x, self.w, self.mu, self.lambda_)
        self.w = self.w[:] + w_delta[:]
        return np.dot(self.w.T, x)[:]
