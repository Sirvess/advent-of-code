def move(pos, direction, value):
    if direction == "N":
        pos[1] += value
    elif direction == "E":
        pos[0] += value
    elif direction == "S":
        pos[1] += -value
    elif direction == "W":
        pos[0] += -value
    return pos


def partA(data):
    def shiftDir(num, shipDirection, direction):
        if direction == "L":
            coeff = -1
        else:
            coeff = 1
        directions = ["N", "E", "S", "W"]
        nextDir = shipDirection
        for i in range(0, int(num)):
            nextDirIndex = directions.index(nextDir) + coeff
            if nextDirIndex > len(directions) - 1:
                nextDirIndex = 0
            elif nextDirIndex < 0:
                nextDirIndex = len(directions) - 1
            nextDir = directions[nextDirIndex]
        return nextDir

    pos = [0, 0]  # Init pos
    shipDirection = "E"  # Init dir
    for action in data:
        command = action[0]
        value = int(action[1:])

        if command == "L" or command == "R":
            shipDirection = shiftDir(value / 90, shipDirection, command)
        elif command == "F":
            pos = move(pos, shipDirection, value)
        else:
            pos = move(pos, command, value)
    return pos


def partB(data):
    def adjustWaypoint(currWaypoint, num, direction):
        nextWaypoint = [0, 0]
        if direction == "L":
            coeff = -1
        else:
            coeff = 1

        if num == 1:
            nextWaypoint[0] = currWaypoint[1] * coeff
            nextWaypoint[1] = -currWaypoint[0] * coeff
        elif num == 2:
            nextWaypoint[0] = -currWaypoint[0]
            nextWaypoint[1] = -currWaypoint[1]
        elif num == 3:
            nextWaypoint[0] = -currWaypoint[1] * coeff
            nextWaypoint[1] = currWaypoint[0] * coeff
        return nextWaypoint

    pos = [0, 0]  # Init pos
    waypoint = [10, 1]  # Init Waypoint
    for action in data:
        command = action[0]
        value = int(action[1:])

        if command == "F":
            pos[0] += value * waypoint[0]
            pos[1] += value * waypoint[1]
        elif command == "R" or command == "L":
            waypoint = adjustWaypoint(waypoint, value / 90, command)
        else:
            waypoint = move(waypoint, command, value)

    return pos


if __name__ == "__main__":
    f = open("day12Input.txt", "r")
    data = f.read().splitlines()
    f.close()

    print("Part A: ", sum([abs(i) for i in partA(data)]))
    print("Part B: ", sum([abs(i) for i in partB(data)]))
