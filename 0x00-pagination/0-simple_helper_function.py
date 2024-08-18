#!/usr/bin/env python3
"""
0-simple_helper_function.py

A simple helper module that provides a function for pagination.

This module is used to calculate the start and end indices for pagination.

Author: Malik Hussein
"""


def index_range(page, page_size):
    """
    Returns a tuple of two integers representing the start and end indices
    for pagination based on the given page and page size.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
