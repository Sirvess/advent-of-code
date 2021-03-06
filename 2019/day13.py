import itertools
from collections import defaultdict


def computergen(data, inputs):
    memory = data.copy()
    i = 0
    relativebase = 0
    while True:
        currmem = memory[i]
        currmemstr = str(currmem).zfill(5)
        currcode = currmemstr[-2:]
        currmode = currmemstr[:-2]
        # mode 0 - position mode, so parameter is position
        # mode 1 - immediate mode, parameter is value
        # mode 2 - relative mode, parameter is position
        if currcode == "01":
            fst = memory[i + 1]
            snd = memory[i + 2]
            trd = memory[i + 3]

            if currmode[-1] == "0":
                fst = memory[fst]
            if currmode[-1] == "2":
                fst = memory[fst + relativebase]
            if currmode[-2] == "0":
                snd = memory[snd]
            if currmode[-2] == "2":
                snd = memory[snd + relativebase]
            if currmode[-3] == "2":
                trd = trd + relativebase

            memory[trd] = fst + snd
            i += 4
        elif currcode == "02":
            fst = memory[i + 1]
            snd = memory[i + 2]
            trd = memory[i + 3]

            if currmode[-1] == "0":
                fst = memory[fst]
            if currmode[-1] == "2":
                fst = memory[fst + relativebase]
            if currmode[-2] == "0":
                snd = memory[snd]
            if currmode[-2] == "2":
                snd = memory[snd + relativebase]
            if currmode[-3] == "2":
                trd = trd + relativebase

            memory[trd] = fst * snd
            i += 4
        elif currcode == "03":
            fst = memory[i + 1]
            if currmode[-1] == "2":
                fst = fst + relativebase
            memory[fst] = inputs.pop(0)
            i += 2
        elif currcode == "04":
            fst = memory[i + 1]
            if currmode[-1] == "0":
                fst = memory[fst]
            if currmode[-1] == "2":
                fst = memory[fst + relativebase]
            yield fst
            i += 2
        elif currcode == "05":
            fst = memory[i + 1]
            snd = memory[i + 2]
            if currmode[-1] == "0":
                fst = memory[fst]
            if currmode[-1] == "2":
                fst = memory[fst + relativebase]
            if currmode[-2] == "0":
                snd = memory[snd]
            if currmode[-2] == "2":
                snd = memory[snd + relativebase]
            if not fst == 0:
                i = snd
            else:
                i += 3
        elif currcode == "06":
            fst = memory[i + 1]
            snd = memory[i + 2]

            if currmode[-1] == "0":
                fst = memory[fst]
            if currmode[-2] == "0":
                snd = memory[snd]
            if currmode[-1] == "2":
                fst = memory[fst + relativebase]
            if currmode[-2] == "2":
                snd = memory[snd + relativebase]
            if fst == 0:
                i = snd
            else:
                i += 3
        elif currcode == "07":
            fst = memory[i + 1]
            snd = memory[i + 2]
            trd = memory[i + 3]

            if currmode[-1] == "0":
                fst = memory[fst]
            if currmode[-1] == "2":
                fst = memory[fst + relativebase]
            if currmode[-2] == "0":
                snd = memory[snd]
            if currmode[-2] == "2":
                snd = memory[snd + relativebase]

            if currmode[-3] == "2":
                trd = trd + relativebase
            if fst < snd:
                memory[trd] = 1
            else:
                memory[trd] = 0
            i += 4
        elif currcode == "08":
            fst = memory[i + 1]
            snd = memory[i + 2]
            trd = memory[i + 3]

            if currmode[-1] == "0":
                fst = memory[fst]
            if currmode[-1] == "2":
                fst = memory[fst + relativebase]
            if currmode[-2] == "0":
                snd = memory[snd]
            if currmode[-2] == "2":
                snd = memory[snd + relativebase]
            if currmode[-3] == "2":
                trd = trd + relativebase

            if fst == snd:
                memory[trd] = 1
            else:
                memory[trd] = 0
            i += 4
        elif currcode == "09":
            fst = memory[i + 1]
            if currmode[-1] == "0":
                fst = memory[fst]
            if currmode[-1] == "2":
                fst = memory[fst + relativebase]
            relativebase += fst
            i += 2
        elif currcode == "99":
            break
    return memory


if __name__ == "__main__":
    f = open("day13.in", "r")
    data = {i: int(code) for i, code in enumerate(f.read().splitlines()[0].split(","))}
    f.close()

    mem = defaultdict(int)
    for x in data:
        mem[x] = data[x]

    computer = computergen(mem.copy(), [])
    output = []
    while True:
        try:
            output.append(next(computer))
        except StopIteration:
            break

    tileids = output[2::3]
    print("Part A:", len([x for x in tileids if x == 2]))
