def move_zeros(numbers):
    write = 0

    for read in range(len(numbers)):
        if numbers[read] != 0:
            numbers[write] = numbers[read]
            write += 1

    for i in range(write, len(numbers)):
        numbers[i] = 0


a = [0, 1, 0, 3, 12]
move_zeros(a)
print(a)

b = [4, 0, 5, 0, 2]
move_zeros(b)
print(b)

c = [1, 2, 3]
move_zeros(c)
print(c)