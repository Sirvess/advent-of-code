if __name__ == "__main__":
    f = open("day15.in", "r")
    data = [
        row.replace(":", "").replace(",", "").split(" ")
        for row in f.read().splitlines()
    ]
    data = {
        row[0]: {
            "cap": int(row[2]),
            "dura": int(row[4]),
            "flav": int(row[6]),
            "tex": int(row[8]),
            "cal": int(row[10]),
        }
        for row in data
    }
    f.close()

    ingredients = set(data)
    dosage = {ingredient: 0 for ingredient in ingredients}

    maxscore = 0
    maxw500cal = 0
    maxingredientsum = 100
    for chocolate in range(0, maxingredientsum + 1):
        for candy in range(0, maxingredientsum + 1):
            for sprinkles in range(0, maxingredientsum + 1):
                for butterscotch in range(0, maxingredientsum + 1):
                    if (
                        not chocolate + candy + sprinkles + butterscotch
                        == maxingredientsum
                    ):
                        continue

                    capscore = 0
                    durascore = 0
                    flavscore = 0
                    texscore = 0
                    calscore = 0

                    for ingredient in ingredients:
                        if ingredient == "Sprinkles":
                            amount = sprinkles
                        elif ingredient == "Butterscotch":
                            amount = butterscotch
                        elif ingredient == "Candy":
                            amount = candy
                        elif ingredient == "Chocolate":
                            amount = chocolate

                        capscore += amount * data[ingredient]["cap"]
                        durascore += amount * data[ingredient]["dura"]
                        flavscore += amount * data[ingredient]["flav"]
                        texscore += amount * data[ingredient]["tex"]
                        calscore += amount * data[ingredient]["cal"]

                    capscore = capscore if capscore > 0 else 0
                    durascore = durascore if durascore > 0 else 0
                    flavscore = flavscore if flavscore > 0 else 0
                    texscore = texscore if texscore > 0 else 0
                    calscore = calscore if calscore > 0 else 0

                    score = capscore * durascore * flavscore * texscore
                    if calscore == 500:
                        if score > maxw500cal:
                            maxw500cal = score
                    if score > maxscore:
                        maxscore = score

    print("Part A:", maxscore)
    print("Part B:", maxw500cal)
