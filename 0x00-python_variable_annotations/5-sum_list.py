#!/usr/bin/python3
"""
type-annotated function sum_list which takes a list
input_list of floats as
argument and returns their sum as a float.
"""


def sum_list(input_list: [float, ...]) -> float:
    """
    function definition
    """
    total = 0.0

    for flt in input_list:
        total += flt
    return total
