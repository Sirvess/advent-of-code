if __name__ == "__main__":
    f = open("day1.in", "r")
    data = f.read().splitlines()[0]
    f.close()

    currsum = 0
    for i, c in enumerate(data):
        if i == len(data) - 1:
            if data[i] == data[0]:
                currsum += int(data[i])
        else:
            if data[i] == data[i + 1]:
                currsum += int(data[i])
    print("Part A:", currsum)

    currsum = 0
    for i, c in enumerate(data):
        oppositeindex = i + len(data) // 2
        if oppositeindex > len(data) - 1:
            oppositeindex = (i + len(data) // 2) - len(data)
        if data[i] == data[oppositeindex]:
            currsum += int(data[i])
    print("Part B:", currsum)
