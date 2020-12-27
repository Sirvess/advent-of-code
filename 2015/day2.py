from itertools import combinations
from functools import reduce

if __name__ == "__main__":
    f = open("day2Input.txt", "r")
    data = f.read().splitlines()
    f.close()

    arr = [[int(y) for y in x] for x in [x.split("x") for x in data]]

    summa = 0
    for subarr in arr:
        combs = [reduce(lambda a, b: a * b, x) for x in combinations(subarr, 2)]
        summa += 2 * sum(combs) + min(combs)
    print("Part A:", summa)

    summa = 0
    for subarr in arr:
        summa += 2 * sum(sorted(subarr)[:-1]) + reduce(lambda a, x: a * x, subarr)
    print("Part B:", summa)
