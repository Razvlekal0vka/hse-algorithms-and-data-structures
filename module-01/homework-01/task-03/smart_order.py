"""Homework 01 — Task 03. Заказ с умом."""


def main():
    n = int(input())
    m = int(input())
    ans = []

    if m <= n:
        ans.append(m)
        return ans

    s = n * (n + 1) // 2
    if s < m:
        ans.append(0)
        return ans

    ost = m
    i = n
    while ost > 0:
        if i > ost:
            i = ost
        ans.append(i)
        ost = ost - i
        i = i - 1

    return ans


if __name__ == "__main__":
    res = main()
    for x in res:
        print(x)
