def traverse(path):
    location = [0, 0]
    visited = set()
    visited.add(tuple(location))
    for c in path:
        if c == ">":
            location[1] += 1
        elif c == "<":
            location[1] -= 1
        elif c == "^":
            location[0] -= 1
        elif c == "v":
            location[0] += 1
        newloc = tuple(location)
        visited.add(newloc)
    return visited


if __name__ == "__main__":
    f = open("day3Input.txt", "r")
    data = f.read().splitlines()
    data = [c for c in data[0]]
    f.close()

    print("Part A:", len(traverse(data)))

    santapath = data[::2]
    robopath = data[1::2]

    jointlyvisited = len(traverse(santapath).union(traverse(robopath)))

    print("Part B:", jointlyvisited)
