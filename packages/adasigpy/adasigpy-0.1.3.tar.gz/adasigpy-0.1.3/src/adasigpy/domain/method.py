from typing import Dict, Callable
import numpy as np

from ..method import lms, nlms


class Method():
    methods: Dict[str, Callable] = {
        "lms": lms,
        "nlms": nlms,
    }


def init_w(method: str, length) -> np.ndarray:
    res: np.ndarray
    if method == "random":
        res = np.random.normal(0, 1., length)
    elif method == "zeros":
        res = np.zeros(length)
    return res
