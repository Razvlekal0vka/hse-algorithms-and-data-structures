"""Homework 01 — Task 05. Так учиться не надо."""


def main():
    n = int(input())
    k = int(input())

    s = n
    p = k - 1
    step = 0

    while True:
        if p >= 3:
            r = p // 3
            if (s - 1) // 2 < r:
                r = (s - 1) // 2
            if r > 0:
                p = p - 3 * r
                s = s - 2 * r
                step = step + 3 * r
                continue

        if p == 0:
            print("Yes")
            print(step + 1)
            return

        if p == 1:
            print("No")
            print(step + 2)
            return

        step = step + 3
        s = s - 2
        p = s - 1


if __name__ == "__main__":
    main()
