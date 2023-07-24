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

    def indexed_dataset(self) -> Dict[int, List]:
        """ Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
               i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(index: Optional[int] = None, page_size:
                        int = 10) -> Dict[str, any]:
        """ implemententation of get hyper"""
        if index is None:
            index = 0
        else:
            assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0
        my_list = []
        data = self.indexed_dataset()
        index = 0 if index is None else index
        keys = sorted(dataset.keys())
        assert index >= 0 and index <= keys[:1]
        for x in keys:
            if i >= index and len(my_list) <= page_size:
                my_list.append(x)

        data = [dataset[y] for y in my_list[:-1]]

        total_rows = len(data)
        next_index = my_list[-1] if len(my_list) - page_size == 1 else None

        return {
            'index': index,
            'data': data,
            'page_size': len(data_page),
            'next_index': next_index
        }
