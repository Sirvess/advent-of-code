import itertools

if __name__ == "__main__":
    f = open("day3.in", "r")
    data = [
        [int(y) for y in x.strip().split(" ") if not y == ""]
        for x in f.read().splitlines()
    ]
    f.close()

    def getValidTriangleCount(data):
        impossiblecount = 0
        for triangle in data:
            permutations = itertools.permutations(triangle)
            faulty = False
            for permutation in permutations:
                sidesum = permutation[0] + permutation[1]
                if permutation[0] + permutation[1] <= permutation[2]:
                    faulty = True
            if faulty:
                impossiblecount += 1
        return len(data) - impossiblecount

    print("Part A:", getValidTriangleCount(data))

    triangles = []

    i = 0
    while i < len(data):
        for j in [0, 1, 2]:
            triangle = [
                data[i][j],
                data[i + 1][j],
                data[i + 2][j],
            ]
            triangles.append(triangle)
        i += 3

    print("Part B:", getValidTriangleCount(triangles))
