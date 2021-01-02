from copy import deepcopy

if __name__ == "__main__":
    f = open("day18.in", "r")
    data = [list(row) for row in f.read().splitlines()]
    f.close()

    def getneighbs(i, j, grid):
        count = 0
        for x in [-1 + i, i, i + 1]:
            for y in [-1 + j, j, j + 1]:
                if x == i and y == j:
                    continue
                elif x < 0 or y < 0 or x > len(grid) - 1 or y > len(grid) - 1:
                    continue
                else:
                    if grid[x][y] == "#":
                        count += 1
        return count

    def iterate(grid):
        olditer = deepcopy(grid)
        newiter = deepcopy(grid)
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                neighbcount = getneighbs(i, j, olditer)
                curr = grid[i][j]
                if curr == "#":
                    if not (neighbcount == 2 or neighbcount == 3):
                        newiter[i][j] = "."
                else:
                    if neighbcount == 3:
                        newiter[i][j] = "#"
        return newiter

    maxiterations = 100
    grid = deepcopy(data)
    for i in range(maxiterations):
        grid = iterate(grid)

    print("Part A:", sum([sum([1 for x in row if x == "#"]) for row in grid]))

    maxiterations = 100
    grid = deepcopy(data)

    grid[0][0] = "#"
    grid[0][len(grid) - 1] = "#"
    grid[len(grid) - 1][len(grid) - 1] = "#"
    grid[len(grid) - 1][0] = "#"
    for i in range(maxiterations):
        grid = iterate(grid)
        grid[0][0] = "#"
        grid[0][len(grid) - 1] = "#"
        grid[len(grid) - 1][len(grid) - 1] = "#"
        grid[len(grid) - 1][0] = "#"

    print("Part B:", sum([sum([1 for x in row if x == "#"]) for row in grid]))
