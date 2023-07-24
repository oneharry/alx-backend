#!/usr/bin/env python3
"""Script for pagination"""
from typing import Tuple, List
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ implementation of pagination"""
    start = (page - 1) * page_size
    end = start + page_size
    return start, end


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """ Initialization method """
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
        """ Implement get page"""
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0

        with open(self.DATA_FILE, 'r') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)
        start, end = index_range(page, page_size)

        if start >= len(data):
            return []

        return data[start:end]
