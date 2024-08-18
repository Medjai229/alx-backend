#!/usr/bin/env python3
"""
1-simple_pagination.py

This module provides a Server class and an index_range function.

The Server class is used to paginate a database of popular baby names.
It provides a get_page method that returns a page of data based on
the given page number and page size. The dataset method is used to
load the data from a CSV file and cache it for subsequent calls.

The index_range function is used to calculate the start and end indices
for pagination based on the given page and page size.

Author: Malik Hussein
"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """
    Returns a tuple of two integers representing the start and end indices
    for pagination based on the given page and page size.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a page of data from the dataset based
        on the given page number and page size.
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        self.dataset()

        IndexRange = index_range(page, page_size)
        page_data = self.dataset()[IndexRange[0]: IndexRange[1]]
        return page_data
