import itertools

if __name__ == "__main__":
    f = open("day17.in", "r")
    data = [int(x) for x in f.read().splitlines()]
    f.close()

    targetsum = 150

    outcombs = []

    for i in range(0, len(data)):
        combs = itertools.combinations(data, i)
        sumcombs = [comb for comb in combs if sum(comb) == targetsum]
        [outcombs.append(comb) for comb in sumcombs]
    print("Part A:", len(outcombs))

    minl = min([len(comb) for comb in outcombs])
    minlcombs = [comb for comb in outcombs if len(comb) == minl]
    print("Part B:", len(minlcombs))
