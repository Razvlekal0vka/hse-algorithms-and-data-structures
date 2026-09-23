"""Homework 02 — Task 03. Без массивов."""

import sys

sys.setrecursionlimit(10000)


def main(s):
    s = s.strip()
    if s == "":
        return
    i = s.find(" ")
    if i == -1:
        print(s, end="")
        return
    num = s[:i]
    rest = s[i + 1 :]
    main(rest)
    print(" ", num, sep="", end="")


if __name__ == "__main__":
    n = int(input())
    line = input()
    main(line)
    print()
