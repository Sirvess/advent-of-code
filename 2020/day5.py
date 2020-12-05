from functools import reduce


def splitRange(lbsplit, ubsplit):
    def reducer(acc, curr):
        if curr == ubsplit:
            return {
                "lower": acc["lower"],
                "upper": acc["lower"] + (acc["upper"] - acc["lower"]) / 2,
            }
        elif curr == lbsplit:
            return {
                "lower": acc["upper"] - (acc["upper"] - acc["lower"]) / 2,
                "upper": acc["upper"],
            }

    return reducer


def toId(instr):
    def getId(col, row):
        return row * 8 + col

    def roundInterval(interval):
        return round((interval["lower"] + interval["upper"]) / 2)

    rowInterval = reduce(splitRange("B", "F"), instr[:7], {"lower": 0, "upper": 127})
    colInterval = reduce(splitRange("R", "L"), instr[7:], {"lower": 0, "upper": 7})
    return getId(roundInterval(colInterval), roundInterval(rowInterval))


if __name__ == "__main__":
    f = open("day5Input.txt", "r")
    data = f.read().splitlines()
    f.close()

    ids = list(map(toId, data))
    maxId = max(ids)
    print("(A), Max: ", maxId)

    missingIds = [i for i in range(0, maxId) if i not in ids]

    myId = [node for node in missingIds if (node - 1 in ids and node + 1 in ids)]
    print("(B), ID: ", myId)
