"""Homework 05 — Task 06. N в степени N."""


def power(base, exp, mod):
    result = 1
    while exp > 0:
        remainder = exp % 2
        if remainder == 1:
            result = result * base
            result = result % mod
        base = base * base
        base = base % mod
        exp = exp // 2
    return result


def main():
    line = input()
    parts = line.split()
    n = int(parts[0])
    mod = int(parts[1])
    answer = power(n, n, mod)
    return answer


if __name__ == "__main__":
    result = main()
    print(result)
