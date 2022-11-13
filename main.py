with open(file='data.txt') as file:
    parenthesis = [list(line) for line in file.read().split("\n")]


auto_complete_map = {"(": ")", "{": "}", "[": "]", "<": ">"}
corrupt_map = {")": "(", "}": "{", ">": "<", "]": "["}
corrupt_points_map = {")": 3, "]": 57, "}": 1197, ">": 25137}
auto_complete_points_map = {")": 1, "]": 2, "}": 3, ">": 4}

corrupted_points = 0
auto_complete_scores = []

for line in parenthesis:
    stack = []
    corrupted_line = False
    incomplete_points = 0

    for char in line:
        if stack and char in corrupt_map:
            if corrupt_map[char] == stack[-1]:
                stack.pop()
            else:
                corrupted_points += corrupt_points_map[char]
                corrupted_line = True
                break
        else:
            stack.append(char)

    if not corrupted_line:
        for char in stack[::-1]:
            incomplete_points = incomplete_points * 5
            incomplete_points += auto_complete_points_map[auto_complete_map[char]]

        auto_complete_scores.append(incomplete_points)


# part one:
print(corrupted_points)

# part two:
output = sorted(auto_complete_scores)
mid = len(output) // 2
print(output[mid])
