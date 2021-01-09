import hashlib

if __name__ == "__main__":
    f = open("day5.in", "r")
    data = f.read().splitlines()[0]
    f.close()

    password = ""
    i = 0
    while len(password) < 8:
        currid = data + str(i)
        hashed = hashlib.md5(currid.encode("utf-8")).hexdigest()
        if hashed.startswith("00000"):
            password += hashed[5]

        i += 1

    print("Part A:", password)

    passworddict = {}
    i = 0
    while len(passworddict) < 8:
        currid = data + str(i)
        hashed = hashlib.md5(currid.encode("utf-8")).hexdigest()
        if hashed.startswith("00000"):
            pos = hashed[5]
            if pos not in ["0", "1", "2", "3", "4", "5", "6", "7"]:
                i += 1
                continue
            if int(pos) in passworddict:
                i += 1
                continue
            passworddict[int(pos)] = hashed[6]

        i += 1

    print("Part B:", "".join([passworddict[x] for x in sorted(passworddict)]))
