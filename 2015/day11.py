if __name__ == "__main__":
    f = open("day11.in", "r")
    data = f.read().splitlines()[0]
    f.close()

    def increment(s):
        i = len(s) - 1
        copy = list(s)
        while s[i] == "z":
            i -= 1
        copy[i] = chr(ord(copy[i]) + 1)
        if i < len(s) - 1:
            for i in range(i + 1, len(copy)):
                copy[i] = "a"
        return "".join(copy)

    def isvalid(s):
        haspair = False
        pairs = set()
        for i in range(0, len(s) - 1):
            if s[i] == s[i + 1]:
                pairs.add(tuple((s[i], s[i + 1])))
            if len(pairs) > 1:
                haspair = True
                break

        hasiol = True if "o" in s or "l" in s or "i" in s else False

        hasthreeconsec = False
        for i in range(0, len(s) - 2):
            if ord(s[i]) + 2 == ord(s[i + 1]) + 1 == ord(s[i + 2]):
                hasthreeconsec = True
                break

        return haspair and (not hasiol) and hasthreeconsec

    currpw = increment(data)
    while not isvalid(currpw):
        currpw = increment(currpw)

    print("Part A:", currpw)
    currpw = increment(currpw)
    while not isvalid(currpw):
        currpw = increment(currpw)
    print("Part B:", currpw)
