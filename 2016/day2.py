if __name__ == "__main__":
    f = open("day2.in", "r")
    data = f.read().splitlines()
    f.close()

    def getcodea(x):
        grid = ["123", "456", "789"]
        pos = [1, 1]
        for char in x:
            if char == "L":
                if pos[1] > 0:
                    pos[1] -= 1
            elif char == "R":
                if pos[1] < 2:
                    pos[1] += 1
            elif char == "U":
                if pos[0] > 0:
                    pos[0] -= 1
            elif char == "D":
                if pos[0] < 2:
                    pos[0] += 1
        return grid[pos[0]][pos[1]]

    print("Part A:", "".join([getcodea(x) for x in data]))

    def getcodeb(x):
        grid = ["00100", "02340", "56789", "0ABC0", "00D00"]
        pos = [2, 0]
        for char in x:
            if char == "L":
                if (pos[1] > 1 and 0 < pos[0] < 4) or pos == [2, 1]:
                    pos[1] -= 1
            elif char == "R":
                if (pos[1] < 3 and 0 < pos[0] < 4) or pos == [2, 3]:
                    pos[1] += 1
            elif char == "U":
                if (1 < pos[0] and 0 < pos[1] < 4) or pos == [1, 2]:
                    pos[0] -= 1
            elif char == "D":
                if (pos[0] < 3 and 0 < pos[1] < 4) or pos == [3, 2]:
                    pos[0] += 1
        return grid[pos[0]][pos[1]]

    print("Part B:", "".join([getcodeb(x) for x in data]))
