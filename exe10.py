def move_zeros(numbers):
    result = []
    zeros = 0

    for i in range(len(numbers)):
        if numbers[i] == 0:
            zeros = zeros + 1
        else:
            result.append(numbers[i])

    for i in range(zeros):
        result.append(0)

    return result


print(move_zeros([0, 1, 0, 3, 12]))
print(move_zeros([1, 2, 3]))
print(move_zeros([0, 0, 5]))