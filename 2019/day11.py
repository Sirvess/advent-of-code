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

    f = open("day11.in", "r")
    data = {i: int(code) for i, code in enumerate(f.read().splitlines()[0].split(","))}
    f.close()

    def runpainter(initialinput, mem):
        inputarr = [initialinput]
        computer = computergen(mem.copy(), inputarr)

        def getblack():
            return "."

        positions = defaultdict(getblack)
        pos = (0, 0)
        bearing = "N"
        while True:
            try:
                fst, snd = next(computer), next(computer)

                # Paint
                positions[pos] = "." if fst == 0 else "#"

                # Update bearing
                if snd == 0:
                    if bearing == "N":
                        bearing = "W"
                    elif bearing == "W":
                        bearing = "S"
                    elif bearing == "S":
                        bearing = "E"
                    elif bearing == "E":
                        bearing = "N"
                elif snd == 1:
                    if bearing == "N":
                        bearing = "E"
                    elif bearing == "E":
                        bearing = "S"
                    elif bearing == "S":
                        bearing = "W"
                    elif bearing == "W":
                        bearing = "N"

                # Move forward
                if bearing == "N":
                    pos = (pos[0], pos[1] - 1)
                elif bearing == "W":
                    pos = (pos[0] - 1, pos[1])
                elif bearing == "E":
                    pos = (pos[0] + 1, pos[1])
                elif bearing == "S":
                    pos = (pos[0], pos[1] + 1)

                # Add input depending on new position
                if positions[pos] == ".":
                    inputarr.append(0)
                else:
                    inputarr.append(1)

            except StopIteration:
                break
        return positions

    mem = defaultdict(int)
    for x in data:
        mem[x] = data[x]

    print("Part A:", len(runpainter(0, mem)))

    print("Part B:")
    # Part B - read from print
    positions = runpainter(1, mem)
    maxy = abs(min([p[1] for p in positions])) + abs(max([p[1] for p in positions]))
    maxx = abs(min([p[0] for p in positions])) + abs(max([p[0] for p in positions]))
    board = [["." for i in range(2 * maxx + 2)] for k in range(2 * maxy + 2)]

    for p in positions:
        print(p, maxy, maxx)
        board[maxy + p[1]][maxx + p[0]] = positions[p]
    for b in board:
        print("".join(b))
