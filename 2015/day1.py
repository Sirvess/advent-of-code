from functools import reduce

if __name__ == "__main__":
    f = open("day1Input.txt", "r")
    data = f.read().splitlines()
    f.close()

    floor = reduce(lambda acc, curr: acc + 1 if curr == "(" else acc - 1, data[0], 0)
    print("Part A:", floor)

    floor = 0
    for i, x in enumerate(list(data[0])):
        if x == "(":
            floor += 1
        elif x == ")":
            floor -= 1
        if floor == -1:
            print("Part B:", i + 1)
            break
