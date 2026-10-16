"""Homework 05 — Task 03. Сортировка выбором максимума."""


def main():
    line = input()
    n = int(line)
    line = input()
    parts = line.split()
    numbers = list(map(int, parts))

    i = n - 1
    while i > 0:
        max_index = 0
        j = 1
        while j <= i:
            current = numbers[j]
            best = numbers[max_index]
            if current > best:
                max_index = j
            j = j + 1
        last = numbers[i]
        numbers[i] = numbers[max_index]
        numbers[max_index] = last
        i = i - 1

    texts = []
    for number in numbers:
        text = str(number)
        texts.append(text)
    result = " ".join(texts)
    print(result)


if __name__ == "__main__":
    main()
