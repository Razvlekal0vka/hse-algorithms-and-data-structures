"""Homework 05 — Task 01. Сортировка бинарными вставками."""


def find_place(a, right, value):
    left = 0
    while left < right:
        mid = (left + right) // 2
        current = a[mid]
        if current <= value:
            left = mid + 1
        else:
            right = mid
    return left


def main():
    line = input()
    n = int(line)
    numbers = []
    if n > 0:
        line = input()
        parts = line.split()
        numbers = list(map(int, parts))

    shifts = 0
    i = 1
    while i < n:
        value = numbers[i]
        place = find_place(numbers, i, value)
        moved = i - place
        shifts = shifts + moved
        block = numbers[place:i]
        numbers[place + 1:i + 1] = block
        numbers[place] = value
        i = i + 1

    texts = []
    for number in numbers:
        text = str(number)
        texts.append(text)
    result = " ".join(texts)
    print(result)
    print(shifts)


if __name__ == "__main__":
    main()
