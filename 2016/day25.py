from copy import deepcopy

if __name__ == "__main__":
    f = open("day25.in", "r")
    data = [act.split() for act in f.read().splitlines()]
    f.close()

    def runcomputer(registers, instructions):
        registerkeys = [x for x in registers]
        i = 0
        output = []
        while i < len(instructions) and len(output) < 10:

            instr = instructions[i]
            actiontype = instr[0]

            if i + 5 < len(instructions):
                cominginstrs = [ins for ins in instructions[i : i + 6]]
                if [ins[0] for ins in cominginstrs] == [
                    "cpy",
                    "inc",
                    "dec",
                    "jnz",
                    "dec",
                    "jnz",
                ]:
                    # Loop, reduce it
                    firstarg = cominginstrs[0][1]
                    if firstarg in registerkeys:
                        firstarg = registers[firstarg]
                    secondarg = cominginstrs[-1][1]
                    if secondarg in registerkeys:
                        secondarg = registers[secondarg]
                    endregindex = cominginstrs[1][1]
                    registers[endregindex] += int(firstarg) * int(secondarg)

                    i += 6
                    continue
            if actiontype == "cpy":
                fr = instr[1]
                to = instr[2]
                # invalid instruction
                if to not in registerkeys:
                    i += 1
                    continue
                if fr in registerkeys:
                    registers[to] = registers[fr]
                else:
                    registers[to] = int(fr)
            elif actiontype == "inc":
                target = instr[1]
                registers[target] += 1
            elif actiontype == "out":
                target = instr[1]
                if target in registerkeys:
                    target = registers[target]
                output.append(int(target))
            elif actiontype == "dec":
                target = instr[1]
                registers[target] -= 1
            elif actiontype == "tgl":
                target = instr[1]
                targetval = registers[target]
                targetindex = targetval + i
                if 0 <= targetindex < len(instructions):
                    totogglestr = instructions[targetindex]
                    totoggleaction = totogglestr[0]
                    if len(totogglestr) == 2:
                        if totoggleaction == "inc":
                            totogglestr[0] = "dec"
                        else:
                            totogglestr[0] = "inc"
                    elif len(totogglestr) == 3:
                        if totogglestr[0] == "jnz":
                            totogglestr[0] = "cpy"
                        else:
                            totogglestr[0] = "jnz"
                    instructions[targetindex] = totogglestr
            elif actiontype == "jnz":
                fr = instr[1]
                if fr in registers:
                    if not registers[fr] == 0:
                        num = instr[2]
                        i += int(num)
                        continue
                elif not ((fr == 0) or fr == "0"):
                    num = instr[2]
                    if num in registerkeys:
                        num = registers[num]
                    i += int(num)
                    continue
            i += 1
        return registers, output

    currout = []
    i = 0
    while not currout == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]:
        registers = {"a": i, "b": 0, "c": 0, "d": 0}
        currout = runcomputer(registers, deepcopy(data))[1]
        i += 1
    print("Part A:", i - 1)
