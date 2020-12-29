import re

if __name__ == "__main__":
    f = open("day8.in", "r")
    data = f.read().splitlines()
    f.close()

    delta = 0
    for row in data:
        asciis = re.findall("\\\\x[0-f]{2}", row[1:-1])

        rem = re.sub("\\\\x[0-f]{2}", "", row[1:-1])

        doublequotes = re.findall('\\\\"', rem)
        rem = re.sub('\\\\"', "", rem)

        backslashes = re.findall("\\\\", rem)
        rem = re.sub("\\\\", "", rem)
        inmemchars = len(rem) + len(doublequotes) + len(asciis) + len(backslashes) // 2

        delta += len(row) - inmemchars
    print("Part A:", delta)

    delta = 0
    for row in data:
        backslashes = len(re.findall("\\\\", row))
        doublequotes = 2 + len(re.findall('"', row))
        delta += backslashes + doublequotes

    print("Part B:", delta)
