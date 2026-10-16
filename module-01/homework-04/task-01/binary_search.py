"""Homework 04 — Task 01. Двоичный поиск."""


def find(a, x):
    left = 0
    right = len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        current = a[mid]
        if current == x:
            index = mid + 1
            return index
        if current < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def main():
    line = input()
    parts = line.split()
    first = list(map(int, parts))
    a = first[1:]

    line = input()
    parts = line.split()
    second = list(map(int, parts))
    queries = second[1:]

    answers = []
    for x in queries:
        index = find(a, x)
        text = str(index)
        answers.append(text)
    result = " ".join(answers)
    return result


if __name__ == "__main__":
    result = main()
    print(result)
