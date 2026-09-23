"""Homework 02 — Task 04. Двоичные строки заданной длины в обратном порядке."""


def main(res, num):
    if num == len(res):
        print(res)
        return
    main(res + '1', num)
    main(res + '0', num)


if __name__ == "__main__":
    n = int(input())
    res = ''
    main(res, n)
