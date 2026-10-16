"""Homework 04 — Task 05. Поиск в отсортированном массиве со сдвигом."""


def find(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        current = nums[mid]
        if current == target:
            return mid
        left_value = nums[left]
        if left_value <= current:
            if left_value <= target and target < current:
                right = mid - 1
            else:
                left = mid + 1
        else:
            right_value = nums[right]
            if current < target and target <= right_value:
                left = mid + 1
            else:
                right = mid - 1
    return -1


def main():
    n = int(input())
    line = input()
    parts = line.split()
    nums = list(map(int, parts))
    nums = nums[:n]
    target = int(input())
    index = find(nums, target)
    return index


if __name__ == "__main__":
    result = main()
    print(result)
