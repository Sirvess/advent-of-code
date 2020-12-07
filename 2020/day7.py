from functools import reduce
import re


# list of: {"colorKey": ColorString, "contains": {"count": string,"color": list of ColorString]}
def parseData(data: list) -> list:
    def parseContainedBags(item):
        countAndColor = item.strip().split(" ", 1)
        count = countAndColor[0]
        color = re.sub("\.", "", re.sub("bag[s]?", "", countAndColor[1])).strip()
        return {"count": count, "color": color}

    def parseRule(row):
        keyValueSplit = re.split("contain[s]?", row)
        colorKey = re.sub("bag[s]?", "", keyValueSplit[0]).strip()

        containing = list(map(parseContainedBags, keyValueSplit[1].split(",")))

        return {"colorKey": colorKey, "contains": containing}

    return list(map(parseRule, data))


if __name__ == "__main__":
    f = open("day7Input.txt", "r")
    data = f.read().splitlines()
    f.close()

    parsedData = parseData(data)

    # Part A
    withGold = set()
    nextColors = ["shiny gold"]

    while len(nextColors) > 0:
        color = nextColors.pop(0)
        wrappingColors = [
            row["colorKey"]
            for row in parsedData
            for containing in row["contains"]
            if color == containing["color"]
        ]
        for wrappingColor in wrappingColors:
            withGold.add(wrappingColor)
            nextColors.append(wrappingColor)

    print("Part A: ", len(withGold))

    # Part B
    def getContainingCount(inColor, parsedData):
        color = list(filter(lambda x: x["colorKey"] == inColor, parsedData))[0]
        if color["contains"][0]["count"] == "no":
            return 0
        else:
            return reduce(
                lambda acc, curr: acc
                + int(curr["count"])
                + int(curr["count"]) * getContainingCount(curr["color"], parsedData),
                color["contains"],
                0,
            )

    print("Part B: ", getContainingCount("shiny gold", parsedData))
