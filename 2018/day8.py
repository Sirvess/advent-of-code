if __name__ == "__main__":
    f = open("day8.in", "r")
    data = [int(x) for x in f.read().splitlines()[0].split()]
    f.close()

    def getmetasum(data):
        childcount, metadatalength = data[0], data[1]
        metastart = 2
        metasum = 0
        for i in range(childcount):
            nlen, nsum = getmetasum(data[metastart:])
            metastart += nlen
            metasum += nsum
        metasum += sum(data[metastart : metastart + metadatalength])
        return metastart + metadatalength, metasum

    totlength, metasum = getmetasum(data)
    print("Part A:", metasum)

    def getrootvalue(data):
        childcount, metadatalength = data[0], data[1]
        metastart = 2
        metasum = 0
        if childcount == 0:
            return sum(data[metastart : metastart + metadatalength])
        else:
            children = {}
            for i in range(childcount):
                children[i + 1] = getrootvalue(data[metastart:])
                nlen, nsum = getmetasum(data[metastart:])
                metastart += nlen
            for i in data[metastart : metastart + metadatalength]:
                if i in children:
                    metasum += children[i]
            return metasum

    print("Part B:", getrootvalue(data))
