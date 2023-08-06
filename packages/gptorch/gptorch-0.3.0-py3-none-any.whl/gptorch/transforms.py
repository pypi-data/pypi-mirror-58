# File: transforms.py
# File Created: Saturday, 24th August 2019 7:05:08 pm
# Author: Steven Atkinson (steven@atkinson.mn)

import torch
from torch.distributions.transforms import Transform


class LowerTriangular(Transform):
    """
    Use for parameters who should always be lower-triangular.

    Note: this is not a bijective transform since the tril() function is not 
    onto.

    Note 2: we help you out by doing tril() in both directions
    """

    def __eq__(self, other):
        return isinstance(other, LowerTriangular)

    def _call(self, x):
        return torch.tril(x)

    def _inverse(self, y):
        return torch.tril(y)
    