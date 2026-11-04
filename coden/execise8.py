def insertion_sort(numbers):
    shifts = 0

    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1

        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            shifts += 1
            j -= 1

        numbers[j + 1] = key

    return numbers, shifts


# Test 1
numbers = [5, 3, 4]
sorted_numbers, total_shifts = insertion_sort(numbers)

print("Sorted list:", sorted_numbers)
print("Total shifts:", total_shifts)


# Test 2
numbers = [8, 5, 3, 2]
sorted_numbers, total_shifts = insertion_sort(numbers)

print("Sorted list:", sorted_numbers)
print("Total shifts:", total_shifts)
