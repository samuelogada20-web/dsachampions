def find_largest(numbers):
    if not numbers:
        return None

    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest


print(find_largest([3, 441, 566, 21, 700, 9])) 
print(find_largest([-10, -5, -2, -18]))      
print(find_largest([]))                       
