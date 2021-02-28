if __name__ == "__main__":
    f = open("day4.in", "r")
    lb, ub = [int(x) for x in f.read().splitlines()[0].split("-")]
    f.close()

    validpasswordcount = 0
    for i in range(lb, ub + 1):
        numstr = str(i)
        nodecrease = True
        for i in range(1, len(numstr)):
            if int(numstr[i]) < int(numstr[i - 1]):
                nodecrease = False
                break
        # can now imply that if there are doubles, chars will be neighbours
        atleastdouble = True if len(set(list(numstr))) < len(numstr) else False

        if atleastdouble and nodecrease:
            validpasswordcount += 1

    print("Part A:", validpasswordcount)

    validpasswordcount = 0
    for i in range(lb, ub + 1):
        numstr = str(i)
        nodecrease = True
        for i in range(1, len(numstr)):
            if int(numstr[i]) < int(numstr[i - 1]):
                nodecrease = False
                break
        double = True if 2 in {numstr.count(i) for i in numstr} else False

        if double and nodecrease:
            validpasswordcount += 1

    print("Part B:", validpasswordcount)
