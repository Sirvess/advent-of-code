def run(data, a, b):
    registers = {"a": a, "b": b}
    i = 0
    while 0 <= i < len(data):
        x = data[i]
        if len(x) > 2:
            ins, fst, snd = x
        else:
            ins, fst = x
        if ins == "hlf":
            registers[fst] /= 2
            i += 1
        elif ins == "tpl":
            registers[fst] *= 3
            i += 1
        elif ins == "inc":
            registers[fst] += 1
            i += 1

        elif ins == "jmp":
            i += int(fst)
        elif ins == "jie":
            if registers[fst] % 2 == 0:
                i += int(snd)
            else:
                i += 1
        elif ins == "jio":
            if registers[fst] == 1:
                i += int(snd)
            else:
                i += 1
    return registers


if __name__ == "__main__":
    f = open("day23.in", "r")
    data = [x.replace(",", "").replace("+", "").split() for x in f.read().splitlines()]
    f.close()

    print("Part A:", run(data, 0, 0)["b"])
    print("Part B:", run(data, 1, 0)["b"])
