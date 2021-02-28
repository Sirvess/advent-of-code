def runcomputer(data, inputs):
    memory = data.copy()
    i = 0
    while True:
        currmem = memory[i]
        currmemstr = str(currmem).zfill(5)
        currcode = currmemstr[-2:]
        currmode = currmemstr[:-2]
        # mode 0 - position mode, so parameter is position
        # mode 1 - immediate mode, parameter is value
        if currcode == "01":
            fst = memory[i + 1]
            snd = memory[i + 2]
            trd = memory[i + 3]

            if currmode[-1] == "0":
                fst = memory[fst]
            if currmode[-2] == "0":
                snd = memory[snd]

            memory[trd] = fst + snd
            i += 4
        elif currcode == "02":
            fst = memory[i + 1]
            snd = memory[i + 2]
            trd = memory[i + 3]

            if currmode[-1] == "0":
                fst = memory[fst]
            if currmode[-2] == "0":
                snd = memory[snd]

            memory[trd] = fst * snd
            i += 4
        elif currcode == "03":
            fst = memory[i + 1]
            memory[fst] = inputs.pop()
            i += 2
        elif currcode == "04":
            fst = memory[i + 1]
            print("OUTPUT", memory[fst])
            i += 2
        elif currcode == "05":
            fst = memory[i + 1]
            snd = memory[i + 2]
            if currmode[-1] == "0":
                fst = memory[fst]
            if currmode[-2] == "0":
                snd = memory[snd]
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
            if currmode[-2] == "0":
                snd = memory[snd]
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
            if currmode[-2] == "0":
                snd = memory[snd]
            if fst == snd:
                memory[trd] = 1
            else:
                memory[trd] = 0
            i += 4
        elif currcode == "99":
            break
    return memory


if __name__ == "__main__":
    f = open("day5.in", "r")
    data = [int(code) for code in f.read().splitlines()[0].split(",")]
    f.close()

    memory = data.copy()
    print("Part A:")
    runcomputer(memory, [1])

    memory = data.copy()
    print("Part B:")
    runcomputer(memory, [5])
