if __name__ == "__main__":
    f = open("day1.in", "r")
    data = [int(x) for x in f.read().splitlines()]
    f.close()

    print("Part A:", sum(data))

    frequencies = set()
    curr, found = 0, False
    while True:
        for x in data:
            curr += x
            if curr in frequencies:
                print("Part B:", curr)
                found = True
                break
            frequencies.add(curr)
        if found:
            break
