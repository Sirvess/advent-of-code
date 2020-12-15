def getNo(iterations, data):
    cache = {}
    for i in range(0, len(data)):
        cache[data[i]] = {"c": 1, "l": i + 1, "r": i + 1}

    prev = data[-1]
    i = len(data) + 1
    while i < iterations + 1:
        nxt = cache[prev]["r"] - cache[prev]["l"]

        if nxt not in cache:
            cache[nxt] = {"c": 1, "l": i, "r": i}
        else:
            cache[nxt]["c"] += 1
            cache[nxt]["l"] = cache[nxt]["r"]
            cache[nxt]["r"] = i

        prev = nxt
        i += 1
    return nxt


if __name__ == "__main__":
    data = [15, 12, 0, 14, 3, 1]

    print("Part A", getNo(2020, data))
    print("Part B", getNo(30000000, data))
