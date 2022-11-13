with open(file='data.txt') as file:
    parenthesis = [list(line) for line in file.read().split("\n")]


AUTO_COMPLETE_MAP = {"(": ")", "{": "}", "[": "]", "<": ">"}
CORRUPT_MAP = {")": "(", "}": "{", ">": "<", "]": "["}
CORRUPT_POINTS_MAP = {")": 3, "]": 57, "}": 1197, ">": 25137}
AUTO_COMPLETE_POINTS_MAP = {")": 1, "]": 2, "}": 3, ">": 4}

corrupted_points = 0
auto_complete_scores = []

for line in parenthesis:
    stack = []
    corrupted_line = False
    incomplete_points = 0

    for char in line:
        if stack and char in CORRUPT_MAP:
            if CORRUPT_MAP[char] == stack[-1]:
                stack.pop()
            else:
                corrupted_points += CORRUPT_POINTS_MAP[char]
                corrupted_line = True
                break
        else:
            stack.append(char)

    if not corrupted_line:
        for char in stack[::-1]:
            incomplete_points = incomplete_points * 5
            incomplete_points += AUTO_COMPLETE_POINTS_MAP[AUTO_COMPLETE_MAP[char]]

        auto_complete_scores.append(incomplete_points)


# part one:
print(corrupted_points)

# part two:
output = sorted(auto_complete_scores)
mid = len(output) // 2
print(output[mid])
