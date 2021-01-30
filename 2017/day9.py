if __name__ == "__main__":
    f = open("day9.in", "r")
    data = f.read()
    f.close()

    garbagecount, score, depth, i, ingarbage = 0, 0, 0, 0, False
    while i < len(data):
        c = data[i]
        if c == "!":
            i += 2
            continue
        if ingarbage and not c == ">":
            garbagecount += 1
        if not ingarbage and c == "{":
            depth += 1
        elif c == "<":
            ingarbage = True
        elif c == ">":
            ingarbage = False
        elif not ingarbage and c == "}":
            score += depth
            depth -= 1
        i += 1

    print("Part A:", score)
    print("Part B:", garbagecount)
