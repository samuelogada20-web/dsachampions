def dfs(node):
    if node in recursion_stack:
        return True

    if node in visited:
        return False

    visited.add(node)
    recursion_stack.add(node)

    for neighbor in graph[node]:
        if dfs(neighbor):
            return True

    recursion_stack.remove(node)
    return False

for node in graph:
    if node not in visited:
        if dfs(node):
            return True

return False
