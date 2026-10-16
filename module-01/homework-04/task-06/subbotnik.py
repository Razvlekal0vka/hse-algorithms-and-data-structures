"""Homework 04 — Task 06. Субботник."""

import sys


def can_form(heights, teams, size, limit):
    count = 0
    i = 0
    n = len(heights)
    last = size - 1
    while i + last < n:
        tall = heights[i + last]
        short = heights[i]
        diff = tall - short
        if diff <= limit:
            count = count + 1
            i = i + size
            if count >= teams:
                return True
        else:
            i = i + 1
    return False


def main():
    data = sys.stdin.read()
    parts = data.split()
    numbers = list(map(int, parts))
    n = numbers[0]
    teams = numbers[1]
    size = numbers[2]
    heights = numbers[3:n + 3]
    heights.sort()

    left = 0
    tallest = heights[n - 1]
    shortest = heights[0]
    right = tallest - shortest
    answer = right
    while left <= right:
        mid = (left + right) // 2
        ok = can_form(heights, teams, size, mid)
        if ok:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer


if __name__ == "__main__":
    result = main()
    print(result)
