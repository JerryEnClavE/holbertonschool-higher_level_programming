#!/usr/bin/python3
"""Python executable file."""


def pascal_triangle(n):
    """Function that returns a list of lists of integers representing
    the Pascal’s triangle of n"""
    triangle = []

    if n <= 0:
        return triangle
    for i in range(n):
        row = [1]
        if i > 0:
            for j in range(i - 1):
                row.append(triangle[i - 1][j] + triangle[i - 1][j + 1])
            row.append(1)
        triangle.append(row)
    return triangle
