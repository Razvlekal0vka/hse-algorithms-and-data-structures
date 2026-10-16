"""Homework 05 — Task 05. Корень кубического уравнения."""


def value_at(x, a, b, c, d):
    value = a
    value = value * x + b
    value = value * x + c
    value = value * x + d
    return value


def main():
    line = input()
    parts = line.split()
    a = int(parts[0])
    b = int(parts[1])
    c = int(parts[2])
    d = int(parts[3])

    left = -2000.0
    right = 2000.0
    step = 0
    while step < 100:
        mid = (left + right) / 2
        current = value_at(mid, a, b, c, d)
        if a > 0:
            if current < 0:
                left = mid
            else:
                right = mid
        else:
            if current > 0:
                left = mid
            else:
                right = mid
        step = step + 1
    root = (left + right) / 2
    return root


if __name__ == "__main__":
    result = main()
    text = "{0:.15f}".format(result)
    print(text)
