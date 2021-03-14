from collections import defaultdict


def computera(data):
    registers = defaultdict(int)
    i = 0
    multcnt = 0
    while i < len(data):
        curr = data[i]
        instr = curr[0]
        if instr == "set":
            x = curr[1]
            y = curr[2]
            if y.isalpha():
                registers[x] = registers[y]
            else:
                registers[x] = int(y)
        elif instr == "sub":
            x = curr[1]
            y = curr[2]
            if y.isalpha():
                registers[x] -= registers[y]
            else:
                registers[x] -= int(y)
        elif instr == "mul":
            multcnt += 1
            x = curr[1]
            y = curr[2]
            if y.isalpha():
                registers[x] *= registers[y]
            else:
                registers[x] *= int(y)
        elif instr == "jnz":
            x = curr[1]
            if x.isalpha():
                x = registers[x]
            else:
                x = int(x)
            if not x == 0:
                y = curr[2]
                if y.isalpha():
                    y = registers[y]
                else:
                    y = int(y)
                i += y
                continue
        i += 1

    print("Part A:", multcnt)


if __name__ == "__main__":
    f = open("day23.in", "r")
    data = [x.split() for x in f.read().splitlines()]
    f.close()

    # Part A
    computera(data)
