#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def cylinder(h, r=1):
    side = 2 * math.pi * r * h
    circle = math.pi * r**2
    full = side + 2 * circle
    return full


if __name__ == '__main__':
    figure1 = cylinder(4, 3)
    figure2 = cylinder(5)
    print(figure1)
    print(figure2)
    figure3 = cylinder(10, 2)
    figure4 = cylinder(r=2, h=10)
    print(figure3)
    print(figure4)
