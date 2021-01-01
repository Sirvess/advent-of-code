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

    maxscore = 0
    maxw500cal = 0
    ingredientsum = 100
    for chocolate in range(0, ingredientsum + 1):
        for candy in range(0, ingredientsum + 1):
            for sprinkles in range(0, ingredientsum + 1):
                for butterscotch in range(0, ingredientsum + 1):
                    if (
                        not chocolate + candy + sprinkles + butterscotch
                        == ingredientsum
                    ):
                        continue

                    capscore = 0
                    durascore = 0
                    flavscore = 0
                    texscore = 0
                    calscore = 0

                    for ingredient in data:
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

                    capscore = max(capscore, 0)
                    durascore = max(durascore, 0)
                    flavscore = max(flavscore, 0)
                    texscore = max(texscore, 0)
                    calscore = max(calscore, 0)

                    score = capscore * durascore * flavscore * texscore
                    if calscore == 500:
                        maxw500cal = max(score, maxw500cal)
                    maxscore = max(maxscore, score)

    print("Part A:", maxscore)
    print("Part B:", maxw500cal)
