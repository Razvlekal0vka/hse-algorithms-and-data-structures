"""Homework 04 — Task 04. Повторяющееся число."""


def main():
    line = input()
    parts = line.split()
    nums = list(map(int, parts))
    left = 1
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        count = 0
        for number in nums:
            if number <= mid:
                count = count + 1
        if count > mid:
            right = mid
        else:
            left = mid + 1
    return left


if __name__ == "__main__":
    result = main()
    print(result)
