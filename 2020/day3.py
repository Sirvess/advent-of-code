import re
import functools

# Define chosen slope by setting steps right and down per iteration
def countTrees(right, down, data):
    i = 0
    j = 0
    treeCount = 0

    while j < len(data):
        if data[j][i] == "#":
            treeCount = treeCount + 1
        # Repeating pattern
        i = (i + right) % len(data[0])

        j = j + down

    return treeCount


partBpatterns = [
    {"right": 1, "down": 1},
    {"right": 3, "down": 1},
    {"right": 5, "down": 1},
    {"right": 7, "down": 1},
    {"right": 1, "down": 2},
]


if __name__ == "__main__":
    f = open("day3Input.txt", "r")
    data = f.read().splitlines()
    f.close()

    # Part A
    print("Part A trees: ", countTrees(3, 1, data))

    # Part B
    print(
        "Part B trees: ",
        functools.reduce(
            lambda a, b: a * b,
            map(
                lambda pattern: countTrees(pattern["right"], pattern["down"], data),
                partBpatterns,
            ),
        ),
    )
