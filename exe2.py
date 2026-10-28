def find_smallest(numbers):
    if not numbers:
        return None

    smallest = numbers[0]

    for number in numbers:
        if number < smallest:
            smallest = number

    return smallest


print(find_smallest([0, 388, 612, 156, 10]))
print(find_smallest([-3, -10, -1, -6]))
print(find_smallest([]))