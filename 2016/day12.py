if __name__ == "__main__":
    f = open("day12.in", "r")
    data = [act.split(" ") for act in f.read().splitlines()]
    f.close()

    def runcomputer(registers, instructions):
        i = 0
        while i < len(data):
            instr = data[i]
            actiontype = instr[0]
            if actiontype == "cpy":
                fr = instr[1]
                to = instr[2]
                if fr in ["a", "b", "c", "d"]:
                    registers[to] = registers[fr]
                else:
                    registers[to] = int(fr)
            elif actiontype == "inc":
                target = instr[1]
                registers[target] += 1
            elif actiontype == "dec":
                target = instr[1]
                registers[target] -= 1
            elif actiontype == "jnz":
                fr = instr[1]
                if fr in registers:
                    if not registers[fr] == 0:
                        num = instr[2]
                        i += int(num)
                        continue
                elif not (fr == 0):
                    num = instr[2]
                    i += int(num)
                    continue
            i += 1
        return registers

    registers = {"a": 0, "b": 0, "c": 0, "d": 0}
    print("Part A:", runcomputer(registers, data)["a"])

    registers = {"a": 0, "b": 0, "c": 1, "d": 0}
    print("Part B:", runcomputer(registers, data)["a"])
