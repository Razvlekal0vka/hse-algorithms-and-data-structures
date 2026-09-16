"""Homework 01 — Task 02. Постеры."""

import math


def main():
    n = int(input())
    a = int(input())
    b = int(input())

    d = math.gcd(a, b)
    k = a * b // d
    res = (n // a) + (n // b) - (n // k)

    return res


if __name__ == "__main__":
    print(main())
