def count_occurrences(numbers, target):
    count = 0

    for i in range(len(numbers)):
        if numbers[i] == target:
            count = count + 1

    return count


print(count_occurrences([2, 8, 2, 8,], 2))
print(count_occurrences([1, 4, 7], 10))
print(count_occurrences([], 5))