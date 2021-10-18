#!/usr/bin/env python3
'''Complex types'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Returns their sum as a float'''
    add: float = 0
    for i in mxd_lst:
        add += i
    return add
