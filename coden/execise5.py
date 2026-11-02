def most_frequent(numbers):
    if not numbers:
        return None

    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1

    best = numbers[0]
    for num in numbers:
        if counts[num] > counts[best]:
            best = num

    return best


print(most_frequent([2, 5, 2, 8, 2, 5]))
print(most_frequent([4, 7, 7, 4]))
print(most_frequent([]))