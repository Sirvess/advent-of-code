import itertools

if __name__ == "__main__":
    f = open("day3.in", "r")
    data = [[int(y) for y in x.strip().split()] for x in f.read().splitlines()]
    f.close()

    def getValidTriangleCount(data):
        impossiblecount = 0
        sortedTriangles = [sorted(x) for x in data]
        for triangle in sortedTriangles:
            if triangle[0] + triangle[1] <= triangle[2]:
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
