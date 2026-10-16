"""Homework 05 — Task 04. Квадратный корень и квадратный квадрат."""


def main():
    line = input()
    c = float(line)
    left = 0.0
    right = 100000.0
    step = 0
    while step < 100:
        mid = (left + right) / 2
        square = mid * mid
        fourth = square * square
        value = fourth + mid
        if value < c:
            left = mid
        else:
            right = mid
        step = step + 1
    root = (left + right) / 2
    x = root * root
    return x


if __name__ == "__main__":
    result = main()
    text = "{0:.9f}".format(result)
    print(text)
