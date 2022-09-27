#!/usr/bin/python3
"""Module 12-pascal_triangle
returns a list of lists of integers representing
the Pascal's triangle of n.
"""


def pascal_triangle(n):
    """Returns the pascal triangle of n.
    Args:
        -n: size of the triangle
    Returns:
        -a list of list of integers
    """
    if n <= 0:
        return []
    matrix = []
    for i in range(n):
        lil_matrix = []
        num = str(11 ** 1)
        for x in num:
            lil_matrix.append(int(x))
        matrix.append(lil_matrix)
    return matrix
