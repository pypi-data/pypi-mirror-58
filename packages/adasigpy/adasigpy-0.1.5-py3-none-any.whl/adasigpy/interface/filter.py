from abc import ABCMeta, abstractmethod
from typing import Callable, Tuple

from numpy import ndarray


class AdaptiveSignalProcesserABC(metaclass=ABCMeta):
    method: Callable
    n: int
    mu: float
    w_init: str
    domain: str
    lambda_: float

    @abstractmethod
    def __init__(
        self,
        model: str,
        n: int,
        mu: float = 0.01,
        w_init: str = "random",
        domain: str = "freq",
        lambda_: float = 1.0,
    ):
        """
        Abstract Class for AdaptiveSignalProcesser

        Args:
            model (str): Algorithm of filter.
            n (int): Length of filter (and input).
            mu (float, optional): Learning rate. Defaults to 0.01. It should be in range from 0 to 1.
            w_init (str, optional): Initializing method of coef-matrix in filter. Defaults to "random". It should be "random" or "zeros".
            domain (str, optional[FOR USE IN THE FUTURE]): Domain for filtering. Defaults to "freq".
            lambda_ (float, optional): Regularization term. Defaults to 1.0.
        """
        raise NotImplementedError

    def adopt(self, d: ndarray, x: ndarray) -> None:
        """
        adopt filter

        Args:
            d (ndarray): Desired array.
            x (ndarray): Input array.
        """
        raise NotImplementedError

    def apply(self, d: ndarray, x: ndarray) -> Tuple[ndarray, ndarray, ndarray]:
        """
        apply filter to \(x\)

        Args:
            d (ndarray): Desired array (as vector, one dimensional).
            x (ndarray): Input array (as matrix, two dimensional).
        'd' and 'x' should have same length.

        Return:
            y (ndarray): Output array (applied).
            e (ndarray): Error for all samples.
            w (ndarray): Filter coef-matrix.
        """
        raise NotImplementedError
