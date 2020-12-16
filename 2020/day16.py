from functools import reduce


def findInvalids(nearbyTickets, rules):
    invalidTickets = []
    for ticket in nearbyTickets:
        valid = False
        for rule in rulesArr:
            if ticket >= rule[0] and ticket <= rule[1]:
                valid = True
                break
        if valid == False:
            invalidTickets.append(ticket)

    return invalidTickets


def isValidPos(ticketIndex, rulePosition, rulesArr, tickets):
    for ticket in tickets:
        valid = False
        for rule in rulesArr[rulePosition][1:]:
            if ticket[ticketIndex] >= rule[0] and ticket[ticketIndex] <= rule[1]:
                valid = True
                break
        if valid == False:
            return False
    return True


if __name__ == "__main__":
    f = open("day16Input.txt", "r")
    data = [x.split("\n") for x in f.read().strip().split("\n\n")]
    f.close()

    rules = [
        [
            x.split(":")[0],
            *[y.strip().replace("or", "").split("  ") for y in x.split(":")[1:]],
        ]
        for x in data[0]
    ]
    rules = [[rule[0], rule[1][0], rule[1][1]] for rule in rules]

    yourTicket = [int(x) for x in data[1][1:][0].split(",")]
    nearbyTickets = [[int(y) for y in x.split(",")] for x in data[2][1:]]

    rulesArr = []
    for rule in rules:
        fst = [int(x) for x in rule[1].split("-")]
        snd = [int(x) for x in rule[2].split("-")]
        rulesArr.append(fst)
        rulesArr.append(snd)

    invalidTickets = []
    validTicket = []
    for ticket in nearbyTickets:
        invalidValues = findInvalids(ticket, rulesArr)
        if len(invalidValues) == 0:
            validTicket.append(ticket)
        for x in invalidValues:
            invalidTickets.append(x)
    print("Part A", sum(invalidTickets))

    # Part B
    rulesArr = [
        [
            rule[0],
            [int(x) for x in rule[1].split("-")],
            [int(x) for x in rule[2].split("-")],
        ]
        for rule in rules
    ]

    ticketl = range(0, len(validTicket[0]))
    validIndeces = {i: [] for i in ticketl}

    path = {}
    remrules = list(ticketl)
    while len(remrules) > 0:
        remrules = [k for k in remrules if k not in [path[j] for j in path]]
        remindeces = [k for k in list(ticketl) if k not in path]
        for i in remindeces:
            validIndeces[i] = []
            for j in remrules:
                if isValidPos(i, j, rulesArr, validTicket):
                    validIndeces[i].append(j)
            if len(validIndeces[i]) == 1:
                validIndeces[i] = validIndeces[i][0]
                path[i] = validIndeces[i]

    departureKeys = [i for i, x in enumerate(rules) if "departure" in rules[i][0]]
    prodindeces = [x for x in validIndeces if validIndeces[x] in departureKeys]
    print("Part B", reduce(lambda a, x: a * yourTicket[x], prodindeces, 1))
