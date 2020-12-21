if __name__ == "__main__":
    f = open("day21Input.txt", "r")
    data = [x.replace(" (", "|(").split("|") for x in f.read().splitlines()]
    data = [
        {"text": x[0].split(" "), "allergens": x[1][9:-1].strip().split(", ")}
        for x in data
    ]
    f.close()

    allergenmap = {}
    for row in data:
        for allergen in row["allergens"]:
            if not allergen in allergenmap:
                allergenmap[allergen] = set(row["text"])
            else:
                allergenmap[allergen] = allergenmap[allergen].intersection(
                    set(row["text"])
                )

    allergwords = {word for allerg in allergenmap for word in allergenmap[allerg]}

    print(
        "Part A:",
        sum([1 for row in data for word in row["text"] if word not in allergwords]),
    )

    # Part B
    transls = {}
    while len(allergenmap) > 0:
        nextword = ""
        for allerg in allergenmap:
            if len(allergenmap[allerg]) == 1:
                nextword = list(allergenmap[allerg]).pop()
                transls[allerg] = nextword
                del allergenmap[allerg]
                break
        for allerg in allergenmap:
            if nextword in allergenmap[allerg]:
                allergenmap[allerg].remove(nextword)

    # sort translationkeys
    output = [transls[key] for key in sorted(list(transls))]
    print("Part B:", ",".join(output))
