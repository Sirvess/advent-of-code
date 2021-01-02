if __name__ == "__main__":
    f = open("day19.in", "r")
    data = [x for x in f.read().strip().split("\n\n")]
    possiblereplacements = [x.split(" => ") for x in data[0].split("\n")]
    inputmolecule = data[1]
    f.close()

    def getOneReplacements(strtotransform, possiblereplacements):
        # Find only one replacements
        possibilities = set()
        for replacement in possiblereplacements:
            for i, x in enumerate(strtotransform):
                substr = strtotransform[i:]
                if substr.startswith(replacement[0]):
                    newsubstr = (
                        strtotransform[0:i]
                        + replacement[1]
                        + strtotransform[i + len(replacement[0]) :]
                    )
                    possibilities.add(newsubstr)
        return possibilities

    print("Part A:", len(getOneReplacements(inputmolecule, possiblereplacements)))
