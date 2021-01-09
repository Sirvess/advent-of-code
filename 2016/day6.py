import math

if __name__ == "__main__":
    f = open("day6.in", "r")
    data = f.read().splitlines()
    f.close()

    colleng = len(data[0])
    colletters = {i: {} for i in range(colleng)}
    for word in data:
        for j in range(colleng):
            if not word[j] in colletters[j]:
                colletters[j][word[j]] = 0
            colletters[j][word[j]] += 1

    amsg = ""
    bmsg = ""
    for i in range(colleng):
        minl, maxl = math.inf, -math.inf
        currmin, currmax = "", ""
        for w in colletters[i]:
            if colletters[i][w] > maxl:
                maxl = colletters[i][w]
                currmax = w
            if colletters[i][w] < minl:
                minl = colletters[i][w]
                currmin = w
        amsg += currmax
        bmsg += currmin

    print("Part A:", amsg)
    print("Part B:", bmsg)
