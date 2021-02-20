def playgame(players, lastmarble):
    marbles = [0]

    currnode = {"val": 0, "l": None, "r": None}
    currnode["r"] = currnode
    currnode["l"] = currnode

    points = {i: 0 for i in range(players)}
    iteration = 0
    currmarindex = 0
    while iteration < lastmarble:

        iteration += 1
        currplayer = iteration % players

        if iteration % 23 == 0:
            points[currplayer] += iteration

            for i in range(7):
                currnode = currnode["l"]

            points[currplayer] += currnode["val"]

            lnode = currnode["l"]
            rnode = currnode["r"]

            lnode["r"] = rnode
            rnode["l"] = lnode
            currnode = rnode

        else:
            newnode = {"val": iteration, "l": None, "r": None}

            oneright = currnode["r"]
            tworight = oneright["r"]

            oneright["r"] = newnode
            newnode["l"] = oneright

            newnode["r"] = tworight
            tworight["l"] = newnode

            currnode = newnode
    return max([points[i] for i in points])


if __name__ == "__main__":
    f = open("day9.in", "r")
    data = f.read().splitlines()[0].split()
    f.close()

    players, lastmarble = int(data[0]), int(data[-2])

    print("Part A:", playgame(players, lastmarble))
    print("Part B:", playgame(players, lastmarble * 100))
