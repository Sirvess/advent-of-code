if __name__ == "__main__":
    cardpub = 12092626
    doorpub = 4707356

    def transform(subjectnum, startnum):
        currnum = startnum
        currnum *= subjectnum
        currnum = currnum % 20201227
        return currnum

    def findloopsize(target):
        iterations = 1
        curr = 1
        while True:
            curr = transform(7, curr)
            if curr == target:
                return iterations
            iterations += 1
        return iterations

    cardloopsize = findloopsize(cardpub)
    # doorloopsize = findloopsize(doorpub)

    curr = 1
    for i in range(cardloopsize):
        curr = transform(doorpub, curr)

    print("Part A:", curr)
