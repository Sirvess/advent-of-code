import re

if __name__ == "__main__":
    f = open("day5.in", "r")
    data = set(f.read().splitlines())
    f.close()

    nicestrs = set()
    for word in data:
        vowelcount = len(re.findall("[aeiou]", word))

        hasfaulty = True if len(re.findall("(ab)|(cd)|(pq)|(xy)", word)) > 0 else False

        hasdouble = False
        for i in range(0, len(word) - 1):
            if word[i] == word[i + 1]:
                hasdouble = True

        if (vowelcount >= 3) and (hasdouble) and (not hasfaulty):
            nicestrs.add(word)

    print("Part A:", len(nicestrs))

    nicestrs = set()
    for word in data:
        wordlist = list(word)

        hasrep = False
        hasdblpair = False

        for i in range(0, len(wordlist) - 2):
            if wordlist[i] == wordlist[i + 2]:
                hasrep = True

        for i in range(0, len(wordlist) - 1):
            if "".join(wordlist[i : i + 2]) in "".join(wordlist[:i]) or "".join(
                wordlist[i : i + 2]
            ) in "".join(wordlist[i + 2 :]):
                hasdblpair = True

        if (hasrep) and (hasdblpair):
            nicestrs.add(word)
    print("Part B:", len(nicestrs))
