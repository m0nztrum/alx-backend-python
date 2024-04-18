#!/usr/bin/env python3
"""
Task 6: Complex types - mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns sum(float) of mxd_lst"""

    return sum(mxd_lst)
