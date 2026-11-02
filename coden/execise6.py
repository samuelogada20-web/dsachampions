def closest_number(numbers, target):
    closest = numbers[0]

    for num in numbers:
        distance = abs(num - target)
        best_distance = abs(closest - target)

        if distance < best_distance or (distance == best_distance and num < closest):
            closest = num

    return closest


print(closest_number([4, 8, 15, 20], 13))
print(closest_number([8, 12], 10))