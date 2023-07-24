#!/usr/bin/env python3
"""Script for pagination"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ implementation of pagination"""
    start = (page - 1) * page_size
    end = start + page_size
    return start, end
