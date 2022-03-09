#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
    print(list(filter(lambda x: x % 3 == 0, foo)))
    print(list(map(lambda x: x * 2 + 10, foo)))
