#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def cylinder():
    r = float(input())
    h = float(input())
    # площадь боковой поверхности цилиндра:
    side = 2 * math.pi * r * h
    # площадь одного основания цилиндра:
    circle = math.pi * r**2
    # полная площадь цилиндра:
    full = side + 2 * circle
    return full


if __name__ == '__main__':
    square = cylinder()
    print(square)
