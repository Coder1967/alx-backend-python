#!/usr/bin/env python3
"""
module for tenth task
"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    returns the first element of a lost if ot exists
    """
    if lst:
        return lst[0]
    else:
        return None
