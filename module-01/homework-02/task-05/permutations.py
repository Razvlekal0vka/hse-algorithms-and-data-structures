"""Homework 02 — Task 05. Все перестановки заданной длины."""

def main(res, num):
    if num == len(res):
        print(res)
        return
    for i in range(1, num + 1):
        if str(i) not in res:
            main(res + str(i), num)


if __name__ == "__main__":
    n = int(input())
    res = ''
    main(res, n)