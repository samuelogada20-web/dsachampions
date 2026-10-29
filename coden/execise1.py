def second_largest(numbers):
    largest = None
    second = None

    for num in numbers:
        if largest is None or num > largest:
            second = largest
            largest = num

        elif num != largest and (second is None or num > second):
            second = num

    return second


numbers = [10, 5, 8, 10, 3]

result = second_largest(numbers)

print("Numbers:", numbers)
print("Second largest:", result)
