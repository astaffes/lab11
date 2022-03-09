#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def countFood():
    a = int(input())
    b = int(input())
    print("Всего", a + b, "шт.")


if __name__ == '__main__':
    print("Сколько бананов и ананасов для обезьян?")
    countFood()
    print("Сколько жуков и червей для ежей?")
    countFood()
    print("Сколько рыб и моллюсков для выдр?")
    countFood()
