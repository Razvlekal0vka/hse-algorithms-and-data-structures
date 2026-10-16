"""Homework 04 — Task 02. Коровы — в стойла!"""


def can_place(stalls, cows, dist):
    count = 1
    last = stalls[0]
    rest = stalls[1:]
    for x in rest:
        gap = x - last
        if gap >= dist:
            count = count + 1
            last = x
            if count >= cows:
                return True
    return False


def main():
    line = input()
    parts = line.split()
    header = list(map(int, parts))
    cows = header[1]

    line = input()
    parts = line.split()
    stalls = list(map(int, parts))

    left = 0
    first_stall = stalls[0]
    last_stall = stalls[-1]
    right = last_stall - first_stall
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        placed = can_place(stalls, cows, mid)
        if placed:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer


if __name__ == "__main__":
    result = main()
    print(result)
