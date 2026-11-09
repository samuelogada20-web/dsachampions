def longest_consecutive(numbers):
    num_set = set(numbers)
    longest = 0

    for num in num_set:
        # Only start counting if num is the beginning of a sequence
        if num - 1 not in num_set:
            current = num
            length = 1

            while current + 1 in num_set:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest


if __name__ == "__main__":
    tests = [
        ([100, 4, 200, 1, 3, 2], 4),
        ([], 0),
        ([5], 1),
        ([1, 2, 2, 3], 3),
        ([-1, 0, 1], 3),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([10, 30, 50], 1),
    ]

    for numbers, expected in tests:
        result = longest_consecutive(numbers)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: {numbers} -> {result} (expected {expected})")