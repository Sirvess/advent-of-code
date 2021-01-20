if __name__ == "__main__":
    f = open("day20.in", "r")
    data = f.read().splitlines()
    f.close()

    rules = set([tuple((int(ip.split("-")[0]), int(ip.split("-")[1]))) for ip in data])
    sortedrules = sorted(rules, key=lambda rule: rule[0])
    minallowed = 0
    for rule in sortedrules:
        if rule[0] <= minallowed:
            minallowed = max(rule[1] + 1, minallowed)
        else:
            break
    print("Part A:", minallowed)

    numdisallowed = 0
    currmax = 0
    for rule in sortedrules:
        if rule[0] >= currmax:
            numdisallowed += rule[1] + 1 - rule[0]
            currmax = rule[1]
        elif rule[1] > currmax:
            numdisallowed += rule[1] - currmax
            currmax = rule[1]
    amountofIps = 4294967295 + 1  # Start from 0
    print("Part B:", amountofIps - numdisallowed)
