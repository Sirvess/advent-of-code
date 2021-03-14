from collections import defaultdict


def computerb(data, receivelist, sendlist, i, registers):
    while i < len(data):
        curr = data[i]
        instr = curr[0]
        if instr == "snd":
            x = curr[1]
            sendlist.append(registers[x])
        if instr == "rcv":
            x = curr[1]
            if len(receivelist) == 0:
                return "rcv", registers, i
            else:
                registers[x] = receivelist.pop(0)
        elif instr == "set":
            x = curr[1]
            y = curr[2]
            if y.isalpha():
                registers[x] = registers[y]
            else:
                registers[x] = int(y)
        elif instr == "add":
            x = curr[1]
            y = curr[2]
            if y.isalpha():
                registers[x] += registers[y]
            else:
                registers[x] += int(y)
        elif instr == "mul":
            x = curr[1]
            y = curr[2]
            if y.isalpha():
                registers[x] *= registers[y]
            else:
                registers[x] *= int(y)
        elif instr == "mod":
            x = curr[1]
            y = curr[2]
            if y.isalpha():
                registers[x] %= registers[y]
            else:
                registers[x] %= int(y)
        elif instr == "jgz":
            x = curr[1]
            if x.isalpha():
                x = registers[x]
            else:
                x = int(x)
            if x > 0:
                y = curr[2]
                if y.isalpha():
                    y = registers[y]
                else:
                    y = int(y)
                i += y
                continue
        i += 1
    return "terminate", None, None


def run2computers(data):

    registers1, registers2 = defaultdict(int), defaultdict(int)
    registers1["p"], registers2["p"] = 0, 1

    sentTo1, sentTo2 = [], []

    sentTo1Counter = 0
    act1, registers1, index1 = computerb(data, sentTo1, sentTo2, 0, registers1)
    act2, registers2, index2 = computerb(data, sentTo2, sentTo1, 0, registers2)
    while True:
        sentTo1Counter += len(sentTo1)
        if act1 == "rcv" and len(sentTo1) > 0:
            act1, registers1, index1 = computerb(
                data, sentTo1, sentTo2, index1, registers1
            )
        elif act2 == "rcv" and len(sentTo2) > 0:
            act2, registers2, index2 = computerb(
                data, sentTo2, sentTo1, index2, registers2
            )
        else:
            break
    print("Part B:", sentTo1Counter)


def computera(data):

    registers = defaultdict(int)

    lastplayed = None
    i = 0
    while i < len(data):
        curr = data[i]

        instr = curr[0]
        if instr == "snd":
            x = curr[1]
            lastplayed = x
        if instr == "rcv":
            x = curr[1]
            if not x == "0":
                print("Part A:", registers[lastplayed])
                break
        elif instr == "set":
            x = curr[1]
            y = curr[2]
            if y.isalpha():
                registers[x] = registers[y]
            else:
                registers[x] = int(y)
        elif instr == "add":
            x = curr[1]
            y = curr[2]
            if y.isalpha():
                registers[x] += registers[y]
            else:
                registers[x] += int(y)
        elif instr == "mul":
            x = curr[1]
            y = curr[2]
            if y.isalpha():
                registers[x] *= registers[y]
            else:
                registers[x] *= int(y)
        elif instr == "mod":
            x = curr[1]
            y = curr[2]
            if y.isalpha():
                registers[x] %= registers[y]
            else:
                registers[x] %= int(y)
        elif instr == "jgz":
            x = curr[1]
            if x.isalpha():
                x = registers[x]
            else:
                x = int(x)
            if x > 0:
                y = curr[2]
                if y.isalpha():
                    y = registers[y]
                else:
                    y = int(y)
                i += y
                continue
        i += 1


if __name__ == "__main__":
    f = open("day18.in", "r")
    data = [x.split() for x in f.read().splitlines()]
    f.close()

    # Part A
    computera(data)
    # Part B
    run2computers(data)
