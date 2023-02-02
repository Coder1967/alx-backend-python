#!/usr/bin/env python3
"""
type-annotated function 'sum_mixed_list'
which takes a list
input_list of floats as
argument and returns their sum as a float.
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """
    function definition
    """
    total = 0.0

    for flt in mxd_lst:
        total += flt
    return total
