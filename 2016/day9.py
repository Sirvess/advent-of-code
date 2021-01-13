if __name__ == "__main__":
    f = open("day9.in", "r")
    data = f.read().splitlines()[0]
    f.close()

    def decompressStr(data, mode="A"):

        outstr = ""
        i = 0
        while i < len(data):
            if data[i] == "(":
                stop = i + data[i:].index(")")
                nums = data[i + 1 : stop].split("x")
                numchars = int(nums[0])
                repeater = int(nums[1])

                if mode == "B":
                    substr = decompressStr(data[stop + 1 : stop + numchars + 1], "B")
                else:
                    substr = data[stop + 1 : stop + 1 + numchars]

                for j in range(repeater):
                    outstr += substr
                i = stop + numchars + 1
            else:
                outstr += data[i]
                i += 1
        return outstr

    print("Part A:", len(decompressStr(data)))
    print("Part B:", len(decompressStr(data, mode="B")))
