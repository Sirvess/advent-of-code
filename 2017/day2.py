if __name__ == "__main__":
    f = open("day2.in", "r")
    data = [[int(i) for i in row.split("\t")] for row in f.read().splitlines()]
    f.close()

    diffsum = sum([max(row) - min(row) for row in data])
    print("Part A:", diffsum)

    diffsum = 0
    for row in data:
        for i in range(len(row)):
            for j in range(i + 1, len(row)):
                if row[i] % row[j] == 0:
                    diffsum += row[i] // row[j]
                elif row[j] % row[i] == 0:
                    diffsum += row[j] // row[i]

    print("Part B:", diffsum)
