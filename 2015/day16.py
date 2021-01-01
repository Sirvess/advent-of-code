def findSue(knownprops, data, part):
    def isMatch(knownprops, sueprops, part):
        if part == "A":
            for prop in knownprops:
                if prop in sueprops:
                    if not sueprops[prop] == knownprops[prop]:
                        return False
            return True
        elif part == "B":
            for prop in knownprops:
                if prop in sueprops:
                    if prop == "cats" or prop == "trees":
                        if not sueprops[prop] > knownprops[prop]:
                            return False
                    elif prop == "pomeranians" or prop == "goldfish":
                        if not sueprops[prop] < knownprops[prop]:
                            return False
                    else:
                        if not sueprops[prop] == knownprops[prop]:
                            return False
            return True

    for sue in data:
        sueprops = {prop[0]: int(prop[1]) for prop in zip(sue[1::2], sue[2::2])}
        if isMatch(knownprops, sueprops, part):
            return sue[0]


if __name__ == "__main__":
    f = open("day16.in", "r")
    data = [
        row.replace("Sue ", "").replace(":", "").replace(",", "").split(" ")
        for row in f.read().splitlines()
    ]

    f.close()

    knownprops = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }

    print("Part A:", findSue(knownprops, data, "A"))
    print("Part B:", findSue(knownprops, data, "B"))
