if __name__ == "__main__":
    f = open("day8.in", "r")
    data = [row.split() for row in f.read().splitlines()]
    f.close()

    def evalcond(cond, registers):
        firstreg = cond[0]
        if firstreg not in registers:
            registers[firstreg] = 0
        return eval(str(registers[firstreg]) + "".join(cond[1:]))

    anymaxreg = 0
    registers = {}
    for row in data:

        reg = row[0]
        action = row[1]
        value = int(row[2])
        cond = row[4:]
        if not reg in registers:
            registers[reg] = 0
        currregvals = [registers[x] for x in registers]
        anymaxreg = max(anymaxreg, max(currregvals))

        if evalcond(cond, registers):
            if action == "dec":
                registers[reg] -= value
            else:
                registers[reg] += value

    print("Part A:", max([registers[x] for x in registers]))
    print("Part B:", anymaxreg)
