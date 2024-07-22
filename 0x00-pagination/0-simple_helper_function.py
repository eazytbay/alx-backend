#!/usr/bin/env python3

""" A  function called index_range that takes 2 integer arguments (page, page_size)
and returns a tuple containing start index and end index
corresponding to the range of indexes to return in alist
for those particular pagination parameters"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """This function returns a tuple that containing both start and end index
    that corresponds to the range of indexes and returns a list
    """
    x, y = 0, 0
    for z in range(page):
        x = y
        y += page_size
    return (x, y)
