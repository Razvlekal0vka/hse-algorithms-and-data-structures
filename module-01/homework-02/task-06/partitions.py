"""Homework 02 — Task 06. Разбиение на неубывающие слагаемые, обратный порядок."""


def main(res, num, cur, last):
    if cur == num:
        print(res)
        return
    if cur > num:
        return
    i = num - cur
    while i >= last:
        if res == "":
            nxt = str(i)
        else:
            nxt = res + " " + str(i)
        main(nxt, num, cur + i, i)
        i = i - 1


if __name__ == "__main__":
    n = int(input())
    main("", n, 0, 1)
