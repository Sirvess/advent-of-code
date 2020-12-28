import hashlib

if __name__ == "__main__":
    data = "iwrupvqb"

    currnum = 0
    while True:
        currstr = data + str(currnum)
        hashed = hashlib.md5(currstr.encode("utf-8")).hexdigest()
        if hashed.startswith("00000"):
            break
        currnum += 1
    print("Part A:", currnum)

    currnum = 0
    while True:
        currstr = data + str(currnum)
        hashed = hashlib.md5(currstr.encode("utf-8")).hexdigest()
        if hashed.startswith("000000"):
            break
        currnum += 1

    print("Part B:", currnum)
