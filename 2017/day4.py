if __name__ == "__main__":
    f = open("day4.in", "r")
    data = [derp.split() for derp in f.read().splitlines()]
    f.close()

    validphrases = 0
    for row in data:
        words = set()
        for word in row:
            words.add(word)
        if len(words) == len(row):
            validphrases += 1
    print("Part A", validphrases)

    validphrases = 0
    for row in data:
        words = set()
        anagrams = set()
        toadd = True
        for word in row:
            words.add(word)
            if str(sorted(word)) in anagrams:
                toadd = False
                break
            anagrams.add(str(sorted(word)))
        if len(words) == len(row) and toadd:
            validphrases += 1
    print("Part B", validphrases)
