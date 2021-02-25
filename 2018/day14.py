if __name__ == "__main__":
    f = open("day14.in", "r")
    data = int(f.read().splitlines()[0])
    f.close()

    def genlast():
        lengthoflast = 10
        e1, e2 = 0, 1
        recipes = {}
        recipes[e1] = 3
        recipes[e2] = 7
        while True:
            if len(recipes) >= lengthoflast:
                yield len(recipes), "".join(
                    [
                        str(recipes[len(recipes) - lengthoflast + x])
                        for x in range(lengthoflast)
                    ]
                )
            else:
                yield len(recipes), "".join([str(recipes[x]) for x in recipes])
            newscore = recipes[e1] + recipes[e2]
            for c in str(newscore):
                recipes[len(recipes)] = int(c)
            e1 = (e1 + 1 + recipes[e1]) % len(recipes)
            e2 = (e2 + 1 + recipes[e2]) % len(recipes)

    gen = genlast()
    recipelength, recipes = next(gen)
    while recipelength < data + 10:
        recipelength, recipes = next(gen)

    print("Part A", recipes[-10:])

    gen = genlast()
    recipelength, recipes = next(gen)
    while recipes.find(str(data)) == -1:
        recipelength, recipes = next(gen)

    print("Part B", recipelength - 10 + recipes.find(str(data)))
