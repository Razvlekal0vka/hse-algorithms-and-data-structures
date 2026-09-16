"""Homework 01 — Task 01. Световые лампы."""


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    t = 0
    min_c = min(a, b // 2, c)
    t = min_c * 4
    a_ost = a - min_c
    b_ost = b - min_c * 2
    c_ost = c - min_c

    if a_ost > 0:
        t = t + 1
        if b_ost > 0:
            t = t + 1
            b_ost = b_ost - 1
            if c_ost > 0:
                t = t + 1
                if b_ost > 0:
                    t = t + 1

    return t


if __name__ == "__main__":
    print(main())
