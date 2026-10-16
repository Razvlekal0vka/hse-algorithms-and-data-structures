"""Homework 05 — Task 02. Сортировка вставками."""


def main():
    line = input()
    n = int(line)
    line = input()
    parts = line.split()
    numbers = list(map(int, parts))

    i = 1
    while i < n:
        value = numbers[i]
        j = i - 1
        while j >= 0:
            current = numbers[j]
            if current <= value:
                break
            numbers[j + 1] = current
            j = j - 1
        numbers[j + 1] = value
        i = i + 1

    texts = []
    for number in numbers:
        text = str(number)
        texts.append(text)
    result = " ".join(texts)
    print(result)


if __name__ == "__main__":
    main()
