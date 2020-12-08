# typeof data = list of {"op": string,"val": string}
def runComputerPtA(data):
    pointer = 0
    acc = 0
    seen = set()
    while True:
        if pointer in seen:
            break
        seen.add(pointer)

        if data[pointer]["op"] == "jmp":
            pointer += int(data[pointer]["val"])

        elif data[pointer]["op"] == "nop":
            pointer += 1

        elif data[pointer]["op"] == "acc":
            acc += int(data[pointer]["val"])
            pointer += 1

    return acc


# typeof data = list of {"op": string,"val": string}
# Returns False if infinite loop
# If pointer > len(data)-1, program done
def runComputerPtB(data):
    pointer = 0
    acc = 0
    seen = set()
    while True:
        if pointer in seen:
            break
        seen.add(pointer)

        if pointer > len(data) - 1:
            return acc

        if data[pointer]["op"] == "jmp":
            pointer += int(data[pointer]["val"])

        elif data[pointer]["op"] == "nop":
            pointer += 1

        elif data[pointer]["op"] == "acc":
            acc += int(data[pointer]["val"])
            pointer += 1

    return False


# typeof data = list of {"op": string,"val": string}
def createData(data):
    return [{"op": row[0], "val": row[1]} for row in [row.split(" ") for row in data]]


if __name__ == "__main__":
    f = open("day8Input.txt", "r")
    data = f.read().splitlines()
    f.close()

    print("Part A", runComputerPtA(createData(data)))

    # Part B

    pd = createData(data)
    jumpOrNopIndeces = [
        i for i in range(0, len(pd)) if pd[i]["op"] == "jmp" or pd[i]["op"] == "nop"
    ]

    for i in jumpOrNopIndeces:
        pd = createData(data)

        if pd[i]["op"] == "jmp":
            pd[i]["op"] = "nop"
        elif pd[i]["op"] == "nop":
            pd[i]["op"] = "jmp"

        result = runComputerPtB(pd)
        if not result == False:
            print("Part B", result)
            break
