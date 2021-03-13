if __name__ == "__main__":
    f = open("day19.in", "r")
    data = f.read().splitlines()
    f.close()

    startpos = (data[0].find("|"), 0)
    initialbearing = "S"

    path = ""
    pos = startpos
    bearing = initialbearing
    stepcount = 1  # Include initial step
    while True:
        if data[pos[1]][pos[0]] == " ":
            # Packet has arrived
            stepcount -= 1  # Remove last step
            break
        if data[pos[1]][pos[0]] == "+":
            # Direction change
            if bearing in ["N", "S"]:
                east = (pos[0] + 1, pos[1])
                west = (pos[0] - 1, pos[1])
                cands = [("E", east), ("W", west)]
            else:
                south = (pos[0], pos[1] + 1)
                north = (pos[0], pos[1] - 1)
                cands = [("S", south), ("N", north)]
            for cand in cands:
                if not data[cand[1][1]][cand[1][0]] == " ":
                    # Change bearing if found valid direction
                    bearing = cand[0]
                    break
        else:
            path += data[pos[1]][pos[0]]

        # Update position based on bearing
        if bearing == "N":
            pos = (pos[0], pos[1] - 1)
        elif bearing == "W":
            pos = (pos[0] - 1, pos[1])
        elif bearing == "S":
            pos = (pos[0], pos[1] + 1)
        elif bearing == "E":
            pos = (pos[0] + 1, pos[1])
        stepcount += 1

    print("Part A:", "".join(list(filter(lambda x: x not in ["|", "-"], path))))
    print("Part B:", stepcount)
