"""Homework 02 — Task 02. Быстрое возведение в степень."""


def main(a, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / main(a, -n)
    if n % 2 == 0:
        return main(a * a, n // 2)
    return a * main(a, n - 1)


if __name__ == "__main__":
    a = float(input())
    n = int(input())
    print(main(a, n))
