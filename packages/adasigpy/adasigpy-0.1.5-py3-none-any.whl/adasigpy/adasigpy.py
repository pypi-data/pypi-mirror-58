import numpy as np

from .domain.method import Method, init_w
from .interface.filter import AdaptiveSignalProcesserABC


class AdaptiveSignalProcesser(AdaptiveSignalProcesserABC):
    def __init__(self, model, shape, mu, w_init, lambda_):
        self.method = Method.methods[model]
        self.mu = mu
        self.w = init_w(w_init, shape)
        self.lambda_ = lambda_

    def adopt(self, d, x):
        if d.shape != x.shape:
            raise ValueError(
                f"2 arrays should have same length. But now, 'd.shape'  is {d.shape} and 'x.shape' is {x.shape[0]}."
            )
        self.method(d, x, self.w, self.mu, self.lambda_)

    def apply(self, d, x):
        if d.shape != x.shape:
            raise ValueError(
                f"2 arrays should have same length. But now, 'd.shape'  is {d.shape} and 'x.shape' is {x.shape}."
            )
        w_delta = self.method(d, x, self.w, self.mu, self.lambda_)
        self.w = self.w + w_delta
        return self.w
