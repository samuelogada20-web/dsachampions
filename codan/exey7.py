def first_unique(text):
    counts = {}

    for char in text:
        counts[char] = counts.get(char, 0) + 1

    for char in text:
        if counts[char] == 1:
            return char

    return None


print(first_unique("leetcode"))
print(first_unique("aabbcddee"))
print(first_unique("aabbcc"))
print(first_unique("swiss"))
print(first_unique("a"))
print(first_unique("abcdef"))
print(first_unique(""))
print(first_unique("aabbc"))
