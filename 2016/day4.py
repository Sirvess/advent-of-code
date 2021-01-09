if __name__ == "__main__":
    f = open("day4.in", "r")
    data = [row.split("-") for row in f.read().splitlines()]
    f.close()

    validids = []
    for row in data:
        checksumitem = row[-1]
        checksum = checksumitem[checksumitem.index("[") + 1 : -1]
        letters = "".join(row[:-1])
        roomid = checksumitem[: checksumitem.index("[")]

        # Five most common letters
        lettermap = {}
        for c in letters:
            if not c in lettermap:
                lettermap[c] = 0
            lettermap[c] += 1

        lettercount = {}
        for c in lettermap:
            if not lettermap[c] in lettercount:
                lettercount[lettermap[c]] = []
            lettercount[lettermap[c]].append(c)

        # Sort based on alphabetical order
        for count in lettercount:
            lettercount[count] = sorted(lettercount[count])

        letterssortedbypop = sorted(lettercount, reverse=True)

        mostcommonletters = []
        for i in letterssortedbypop:
            for j in lettercount[i]:
                if len(mostcommonletters) == 5:
                    break
                mostcommonletters.append(j)
            if len(mostcommonletters) == 5:
                break

        # mostcommonletters is now correct
        if checksum == "".join(mostcommonletters):
            validids.append(int(roomid))

    print("Part A:", sum(validids))

    for row in data:
        checksumitem = row[-1]
        checksum = checksumitem[checksumitem.index("[") + 1 : -1]
        letters = row[:-1]
        roomid = checksumitem[: checksumitem.index("[")]
        if not int(roomid) in validids:
            continue

        sentence = ""
        for j, letter in enumerate("-".join(letters)):
            oldcode = ord(letter)
            newcode = oldcode
            if letter == "-":
                sentence += " "
                continue
            for i in range(0, int(roomid) % (ord("z") + 1 - ord("a"))):
                newcode += 1
                if newcode > ord("z"):
                    newcode = ord("a")
            sentence += chr(newcode)
        if "north" in sentence:
            print("Part B:", roomid)
            break
