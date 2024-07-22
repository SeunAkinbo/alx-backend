#!/usr/bin/env python3
"""Module - 0-simple_helper_function.py (Helper Function)"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    Returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.

    :param page: integer, 1-indexed page number
    :param page_size: integer, number of items per page
    :return: tuple, (start index, end index)
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
