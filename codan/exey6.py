def missing_number(numbers):
    n = len(numbers)
    expected = n * (n + 1) // 2   # sum of 0..n
    actual = sum(numbers)
    return expected - actual


print(missing_number([3, 0, 1]))                    
print(missing_number([0, 1]))                       
print(missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))  