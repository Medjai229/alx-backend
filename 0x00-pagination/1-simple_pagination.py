#!/usr/bin/env python3
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
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        self.dataset()
        
        IndexRange = index_range(page, page_size)
        page_data = self.dataset()[IndexRange[0]: IndexRange[1]]
        return page_data