from collections import deque

def shortest_path(graph, start, target):
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        node, path = queue.popleft()

        if node == target:
            return path

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None


graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D", "E"],
    "D": ["F"],
    "E": ["F"],
    "F": []
}

print(shortest_path(graph, "A", "F"))
print(shortest_path(graph, "A", "D"))
print(shortest_path(graph, "B", "F"))
print(shortest_path(graph, "A", "A"))
print(shortest_path(graph, "F", "A"))
