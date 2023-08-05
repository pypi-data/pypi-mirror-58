from typing import Callable, Dict, Union, Tuple

import numpy as np

from ..method import lms, nlms


class Method:
    methods: Dict[str, Callable] = {
        "lms": lms,
        "nlms": nlms,
    }


def init_w(method: str, shape: Union[int, Tuple[int]]) -> np.ndarray:
    res: np.ndarray
    if method == "random":
        res = np.random.normal(0, 0.5, shape)
    elif method == "zeros":
        res = np.zeros(shape)
    return res
