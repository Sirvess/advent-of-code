import re
from json import loads

if __name__ == "__main__":
    f = open("day12.in", "r")
    data = f.read().splitlines()[0]
    f.close()

    print("Part A:", sum([int(i) for i in re.findall("-?[0-9]+", data)]))

    def sumtraverse(jsondata):
        if type(jsondata) is int:
            return jsondata
        elif type(jsondata) is dict:
            if "red" in jsondata.values():
                return 0
            else:
                return sum([sumtraverse(jsondata[x]) for x in jsondata])
        elif type(jsondata) is list:
            return sum([sumtraverse(x) for x in jsondata])
        else:
            return 0

    print("Part B:", sumtraverse(loads(data)))
