"""Homework 02 — Task 01. Факториал числа."""


def main(n, res):
    if n == 0:
        return 1
    elif n < 0:
        return '-'
    else:
        res = n * main(n - 1, res)
    return res


if __name__ == "__main__":
    n = int(input())
    res = 0
    print(main(n, res))
