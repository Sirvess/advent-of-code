import re


def getSequences(row):
    hypernetSequences = re.findall("\[([a-z]+?)\]", row)
    supernetsFromLeft = re.findall("([a-z]+)[\[]", row)
    supernetsFromRight = re.findall("[\]]([a-z]+)", row)
    supernetSequences = list(set(supernetsFromLeft + supernetsFromRight))
    return hypernetSequences, supernetSequences


def hasAbba(sequences):
    for cand in sequences:
        for i, c in enumerate(cand):
            if i == 0:
                continue
            if i == len(cand) - 2:
                break
            if (
                (cand[i] == cand[i + 1])
                and (cand[i - 1] == cand[i + 2])
                and not (cand[i] == cand[i - 1])
            ):
                return True
    return False


def getAbas(sequences):
    abas = []
    for cand in sequences:
        for i, c in enumerate(cand):
            if i == len(cand) - 2:
                break
            if (cand[i] == cand[i + 2]) and not (cand[i] == cand[i + 1]):
                abas.append(cand[i : i + 3])
    return abas


if __name__ == "__main__":
    f = open("day7.in", "r")
    data = f.read().splitlines()
    f.close()

    tlsCounter = 0

    for row in data:
        hypernetSequences, supernetSequences = getSequences(row)
        inInners = hasAbba(hypernetSequences)
        inOuters = hasAbba(supernetSequences)

        if (not inInners) and inOuters:
            tlsCounter += 1

    print("Part A:", tlsCounter)

    sslCounter = 0
    for row in data:
        hypernetSequences, supernetSequences = getSequences(row)
        hypernetAbas = getAbas(hypernetSequences)
        supernetAbas = getAbas(supernetSequences)
        for aba in hypernetAbas:
            invertedAba = aba[1] + aba[0] + aba[1]
            if invertedAba in supernetAbas:
                sslCounter += 1
                break

    print("Part B:", sslCounter)
