"""Homework 04 — Task 08. Копии."""


def can_copy(time, count, fast, slow):
    if time < fast:
        return False
    made = time // fast
    rest = time - fast
    extra = rest // slow
    made = made + extra
    if made >= count:
        return True
    return False


def main():
    line = input()
    parts = line.split()
    count = int(parts[0])
    first = int(parts[1])
    second = int(parts[2])
    fast = first
    slow = second
    if second < first:
        fast = second
        slow = first
    left = 0
    right = count * fast
    answer = right
    while left <= right:
        mid = (left + right) // 2
        ok = can_copy(mid, count, fast, slow)
        if ok:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer


if __name__ == "__main__":
    result = main()
    print(result)
