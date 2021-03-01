if __name__ == "__main__":
    f = open("day8.in", "r")
    data = f.read().splitlines()[0]
    f.close()

    w = 25
    h = 6

    minz = w * h
    score = w * h
    images = []
    i = 0
    while i < len(data):
        x = data[i : i + w * h]
        zeros = x.count("0")
        if zeros < minz:
            minz = zeros
            score = x.count("1") * x.count("2")
        images.append(x)
        i += w * h
    print("Part A:", score)

    layers = {}
    for image in images:
        for i, c in enumerate(image):
            if not i in layers:
                layers[i] = ""
            layers[i] += c

    def reducelayer(s):
        for c in s:
            if c == "0":
                return "."
            elif c == "1":
                return "#"
        return "0"

    print("Part B:")
    readablelayers = "".join([reducelayer(layers[x]) for x in layers])
    for i in range(h):
        print(readablelayers[i * w : i * w + w])
