def circuit(data, boverride=None):
    wires = {}

    assigned = set()
    while len(assigned) < len(data):
        for i, x in enumerate(data):
            target = x[1]
            if i not in assigned:
                if len(x[0]) == 1:
                    if x[0][0].isdigit():
                        if target == "b" and boverride:
                            wires[target] = boverride
                        else:
                            wires[target] = int(x[0][0])
                        assigned.add(i)
                    elif x[0][0] in wires:
                        wires[target] = wires[x[0][0]]
                        assigned.add(i)
                elif x[0][1] == "AND":
                    if (
                        (x[0][0] in wires and x[0][2] in wires)
                        or (x[0][0].isdigit() and x[0][2] in wires)
                        or (x[0][2].isdigit() and x[0][0] in wires)
                        or (x[0][0].isdigit() and x[0][2].isdigit())
                    ):
                        ltar = int(x[0][0]) if x[0][0].isdigit() else wires[x[0][0]]
                        rtar = int(x[0][2]) if x[0][2].isdigit() else wires[x[0][2]]
                        wires[target] = ltar & rtar
                        assigned.add(i)
                elif x[0][1] == "OR":
                    if (
                        (x[0][0] in wires and x[0][2] in wires)
                        or (x[0][0].isdigit() and x[0][2] in wires)
                        or (x[0][2].isdigit() and x[0][0] in wires)
                        or (x[0][0].isdigit() and x[0][2].isdigit())
                    ):
                        ltar = int(x[0][0]) if x[0][0].isdigit() else wires[x[0][0]]
                        rtar = int(x[0][2]) if x[0][2].isdigit() else wires[x[0][2]]
                        wires[target] = ltar | rtar
                        assigned.add(i)
                elif x[0][1] == "RSHIFT":
                    if (
                        (x[0][0] in wires and x[0][2] in wires)
                        or (x[0][0].isdigit() and x[0][2] in wires)
                        or (x[0][2].isdigit() and x[0][0] in wires)
                        or (x[0][0].isdigit() and x[0][2].isdigit())
                    ):
                        ltar = int(x[0][0]) if x[0][0].isdigit() else wires[x[0][0]]
                        rtar = int(x[0][2]) if x[0][2].isdigit() else wires[x[0][2]]
                        wires[target] = ltar >> rtar

                        assigned.add(i)
                elif x[0][1] == "LSHIFT":
                    if (
                        (x[0][0] in wires and x[0][2] in wires)
                        or (x[0][0].isdigit() and x[0][2] in wires)
                        or (x[0][2].isdigit() and x[0][0] in wires)
                        or (x[0][0].isdigit() and x[0][2].isdigit())
                    ):
                        ltar = int(x[0][0]) if x[0][0].isdigit() else wires[x[0][0]]
                        rtar = int(x[0][2]) if x[0][2].isdigit() else wires[x[0][2]]
                        wires[target] = ltar << rtar
                        assigned.add(i)
                elif x[0][0] == "NOT":
                    if x[0][1].isdigit() or x[0][1] in wires:
                        ltar = int(x[0][1]) if x[0][1].isdigit() else wires[x[0][1]]
                        wires[target] = ~ltar
                        assigned.add(i)
    return wires


if __name__ == "__main__":
    f = open("day7.in", "r")
    data = f.read().splitlines()
    data = [x.split(" -> ") for x in data]
    data = [[x[0].split(" "), x[1]] for x in data]
    f.close()

    wiresA = circuit(data, False)
    print("Part A:", wiresA["a"])
    print("Part B:", circuit(data, int(wiresA["a"]))["a"])
    # TODO: Set B override with value from A
