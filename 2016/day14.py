import hashlib


def find64thPartA(data):
    index = 0
    foundkeys = 0
    while foundkeys < 65:
        cand = data + str(index)
        threerepcand = hashlib.md5(cand.encode("utf-8")).hexdigest()
        for l, c in enumerate(threerepcand[:-2]):
            if threerepcand[l] == threerepcand[l + 1] == threerepcand[l + 2]:
                for j in range(1001):
                    candtwo = data + str(index + j + 1)
                    fiverepcand = hashlib.md5(candtwo.encode("utf-8")).hexdigest()

                    for k, c in enumerate(fiverepcand[:-4]):

                        if k > 0 and fiverepcand[k] == fiverepcand[k - 1]:
                            continue
                        if (
                            fiverepcand[k]
                            == fiverepcand[k + 1]
                            == fiverepcand[k + 2]
                            == fiverepcand[k + 3]
                            == fiverepcand[k + 4]
                            == threerepcand[l]
                        ):
                            foundkeys += 1
                            if foundkeys == 64:
                                return index
                break
        index += 1


def find64thPartB(data):
    index = 0
    foundkeys = 0
    foundhashes = {}
    while foundkeys < 65:
        cand = data + str(index)
        if cand in foundhashes:
            threerepcand = foundhashes[cand]
        else:
            threerepcand = hashlib.md5(cand.encode("utf-8")).hexdigest()
            foundhashes[cand] = threerepcand
        for z in range(2016):
            if not threerepcand in foundhashes:
                foundhashes[threerepcand] = hashlib.md5(
                    threerepcand.encode("utf-8")
                ).hexdigest()
            threerepcand = foundhashes[threerepcand]
        for l, c in enumerate(threerepcand[:-2]):
            if threerepcand[l] == threerepcand[l + 1] == threerepcand[l + 2]:
                for j in range(1001):
                    candtwo = data + str(index + j + 1)
                    if candtwo in foundhashes:
                        fiverepcand = foundhashes[candtwo]
                    else:
                        fiverepcand = hashlib.md5(candtwo.encode("utf-8")).hexdigest()
                        foundhashes[candtwo] = fiverepcand

                    for p in range(2016):
                        if not fiverepcand in foundhashes:
                            foundhashes[fiverepcand] = hashlib.md5(
                                fiverepcand.encode("utf-8")
                            ).hexdigest()
                        fiverepcand = foundhashes[fiverepcand]
                    for k, c in enumerate(fiverepcand[:-4]):

                        if k > 0 and fiverepcand[k] == fiverepcand[k - 1]:
                            continue
                        if (
                            fiverepcand[k]
                            == fiverepcand[k + 1]
                            == fiverepcand[k + 2]
                            == fiverepcand[k + 3]
                            == fiverepcand[k + 4]
                            == threerepcand[l]
                        ):
                            foundkeys += 1
                            if foundkeys == 64:
                                return index
                break
        index += 1


if __name__ == "__main__":
    f = open("day14.in", "r")
    data = f.read().splitlines()[0]
    f.close()

    print("Part A:", find64thPartA(data))
    print("Part B:", find64thPartB(data))
