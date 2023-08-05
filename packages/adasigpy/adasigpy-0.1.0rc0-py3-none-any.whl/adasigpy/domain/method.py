from typing import Dict, Callable
import numpy as np

from ..method import lms, nlms


class Method():
    methods: Dict[str, Callable] = {
        "lms": lms,
        "nlms": nlms,
    }


class InitFilterCoefMatrix():
    methods: Dict[str, Callable] = {
        "random": np.random.normal,
        "zeros": np.zeros
    }
