"""Homework 04 — Task 03. Дипломы."""


def can_fit(side, width, height, count):
    along_width = side // width
    along_height = side // height
    total = along_width * along_height
    return total >= count


def main():
    line = input()
    parts = line.split()
    width = int(parts[0])
    height = int(parts[1])
    count = int(parts[2])
    left = max(width, height)
    right = left * count
    answer = right
    while left <= right:
        mid = (left + right) // 2
        fits = can_fit(mid, width, height, count)
        if fits:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer


if __name__ == "__main__":
    result = main()
    print(result)
