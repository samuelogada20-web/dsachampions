def valid_parentheses(text):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []

    for char in text:
        if char in pairs.values():
            # Opening bracket: remember it
            stack.append(char)
        elif char in pairs:
            # Closing bracket: must match the most recent opening one
            if not stack or stack.pop() != pairs[char]:
                return False

    # Valid only if nothing is left open
    return len(stack) == 0


if __name__ == "__main__":
    tests = [
        ("{[()]}", True),
        ("([)]", False),
        ("((()))", True),
        ("{[}", False),
        ("", True),
        ("(", False),
        (")", False),
        ("()[]{}", True),
        ("(((", False),
        ("())", False),
        ("a(b[c]{d}e)f", True),
    ]

    for text, expected in tests:
        result = valid_parentheses(text)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: {text!r} -> {result} (expected {expected})")