if __name__ == "__main__":
    f = open("day20.in", "r")
    data = int(f.read().splitlines()[0])
    f.close()

    def findindex(iterations, target, partb=False):
        presents = {i: i * 10 for i in range(1, iterations + 1)}
        if partb:
            presents = {i: i * 11 for i in range(1, iterations + 1)}
        i = 1
        while presents[i] < data and i < iterations:
            j = i + i
            count = 0
            while j < iterations:
                presents[j] += i * 10
                if partb:
                    presents[j] += i
                j += i
                count += 1
                if partb and count == 50:
                    break
            i += 1
        return i, presents[i]

    indexval = 0
    iterations = 100
    while indexval < data:
        index, indexval = findindex(iterations, data)
        if indexval >= data:
            print("Part A:", index)
        else:
            print("Not enough iterations, increasing...")
        iterations = iterations * 10

    indexval = 0
    iterations = 100
    while indexval < data:
        index, indexval = findindex(iterations, data, True)
        if indexval >= data:
            print("Part B:", index)
        else:
            print("Not enough iterations, increasing...")
        iterations = iterations * 10
