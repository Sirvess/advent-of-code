def runcomputer(data):
    memory = data.copy()
    i = 0
    while True:
        x = memory[i]
        if x == 1:
            fst = memory[i + 1]
            snd = memory[i + 2]
            trd = memory[i + 3]
            memory[trd] = memory[fst] + memory[snd]
            i += 4
        elif x == 2:
            fst = memory[i + 1]
            snd = memory[i + 2]
            trd = memory[i + 3]
            memory[trd] = memory[fst] * memory[snd]
            i += 4
        elif x == 99:
            break
    return memory


if __name__ == "__main__":
    f = open("day2.in", "r")
    data = [int(x) for x in f.read().splitlines()[0].split(",")]
    f.close()

    memory = data.copy()
    memory[1] = 12
    memory[2] = 2
    print("Part A:", runcomputer(memory)[0])

    for i in range(100):
        for j in range(100):
            memory = data.copy()
            memory[1] = i
            memory[2] = j
            result = runcomputer(memory)[0]
            if result == 19690720:
                print("Part B:", 100 * i + j)
                break
