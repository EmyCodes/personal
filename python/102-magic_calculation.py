#!/usr/bin/python3
"""
Python bytecode:
"""


def magic_calculation(a, b):
    """Python bytecode"""
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        sub(a, b)
