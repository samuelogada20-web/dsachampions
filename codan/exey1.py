def two_sum(numbers, target):
    seen = {}

    for i, num in enumerate(numbers):
        needed = target - num

        if needed in seen:
            return [seen[needed], i]

        seen[num] = i

    return None

print(two_sum([2, 7, 11, 15], 9))
# [0, 1]

print(two_sum([3, 2, 4], 6))
# [1, 2]

print(two_sum([3, 3], 6))
# [0, 1]

print(two_sum([1, 2, 3], 10))
# None
