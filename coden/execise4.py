from collections import deque


def reverse_first(queue, k):
    stack = []

    for _ in range(k):
        stack.append(queue.popleft())

    while stack:
        queue.append(stack.pop())

    for _ in range(len(queue) - k):
        queue.append(queue.popleft())


q1 = deque([10, 20, 30, 40, 50])
reverse_first(q1, 3)
print(list(q1))

q2 = deque([1, 2, 3, 4])
reverse_first(q2, 2)
print(list(q2))