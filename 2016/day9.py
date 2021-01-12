if __name__ == "__main__":
    f = open("day9.in", "r")
    data = f.read().splitlines()[0]
    f.close()

    outstr = ""
    i = 0
    while i < len(data):
        if data[i] == "(":
            stop = i + data[i:].index(")")
            nums = data[i + 1 : stop].split("x")
            numchars = int(nums[0])
            repeater = int(nums[1])
            for j in range(repeater):
                outstr += data[stop + 1 : stop + 1 + numchars]
            i = stop + numchars + 1
        else:
            outstr += data[i]
            i += 1
    print("Part A:", len(outstr))
