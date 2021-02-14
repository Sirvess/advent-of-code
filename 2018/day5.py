if __name__ == "__main__":
    f = open("day5.in", "r")
    data = f.read().splitlines()[0]
    f.close()

    def reducestr2length(s):
        while True:
            newstr = ""
            i = 0
            while i < len(s):
                if (
                    not i == len(s) - 1
                    and not (s[i] == s[i + 1])
                    and (s[i] == s[i + 1].upper() or s[i].upper() == s[i + 1])
                ):
                    i += 2
                else:
                    newstr += s[i]
                    i += 1

            if len(s) == len(newstr):
                break
            s = newstr
        return len(s)

    print("Part A:", reducestr2length(data))

    minl = len(data)
    for c in "abcdefghijklmnopqrstuvwxyz":
        snew = reducestr2length(data.replace(c, "").replace(c.upper(), ""))
        if snew < minl:
            minl = snew
    print("Part B:", minl)
