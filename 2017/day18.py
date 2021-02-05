if __name__ == "__main__":
    f = open("day18.in", "r")
    data = [x.split() for x in f.read().splitlines()]

    f.close()

    registers = {}
    soundsplayed = []
    ptr = 0
    while 0 <= ptr < len(data):
        act = data[ptr]
        a = act[0]
        b = act[1]
        if len(act) == 3:
            c = act[2]
            if c in registers:
                c = registers[c]
            else:
                c = int(c)
        if b not in registers:
            registers[b] = 0
        if a == "snd":
            if b in registers:
                b = registers[b]
            else:
                b = int(b)
            soundsplayed.append(b)
        elif a == "set":
            registers[b] = c
        elif a == "add":
            registers[b] += c
        elif a == "mul":
            registers[b] *= c
        elif a == "mod":
            registers[b] %= c
        elif a == "rcv":
            if len(soundsplayed) > 0:
                c = soundsplayed.pop()
            else:
                c = 0
            if b in registers:
                b = registers[b]
            else:
                b = int(b)
            if not int(b) == 0:
                print("Part A:", c)
                break
        elif a == "jgz":
            if b in registers:
                b = registers[b]
            else:
                b = int(b)
            if b > 0:
                ptr += c
                continue
            else:
                ptr += 1
                continue
        ptr += 1
