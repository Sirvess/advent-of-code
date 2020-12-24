from copy import deepcopy


if __name__ == "__main__":
    # f = open("day24Test.txt", "r")
    f = open("day24Input.txt", "r")
    data = f.read().splitlines()
    f.close()

    tilepos = {}
    for j, row in enumerate(data):
        pos = [0, 0]
        i = 0
        while i < len(row):
            if row[i] == "s" or row[i] == "n":
                c = "x"
                if not i == len(row) - 1:
                    if row[i + 1] == "e" or row[i + 1] == "w":
                        c = row[i] + row[i + 1]
                        i += 2
                else:
                    c = row[i]
                    i += 1
            else:
                c = row[i]
                i += 1
            if c == "e":
                pos[0] += 2
            elif c == "w":
                pos[0] -= 2
            elif c == "nw":
                pos[0] -= 1
                pos[1] -= 1
            elif c == "ne":
                pos[0] += 1
                pos[1] -= 1
            elif c == "se":
                pos[0] += 1
                pos[1] += 1
            elif c == "sw":
                pos[0] -= 1
                pos[1] += 1

        key = tuple(pos)
        if key in tilepos:
            if tilepos[key] == "white":
                tilepos[key] = "black"
            else:
                tilepos[key] = "white"
        else:
            tilepos[key] = "black"
    print("Part A:", sum([1 for key in tilepos if tilepos[key] == "black"]))
