# https://leetcode.com/problems/triangle/
# Medium
from typing import List


def minimum_total(triangle: List[List[int]]) -> int:
    n = len(triangle)
    min_path = triangle[-1]

    for i in range(n - 2, -1, -1):
        for j in range(len(triangle[i])):
            min_path[j] = triangle[i][j] + min(min_path[j], min_path[j + 1])

    return min_path[0]
