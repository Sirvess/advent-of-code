from collections import defaultdict
from copy import deepcopy
import re
import math

if __name__ == "__main__":
    f = open("day20.in", "r")
    data = [
        str(re.sub("<|>,|>|[p|a|v]=", "", x)).split() for x in f.read().splitlines()
    ]
    f.close()

    initialpoints = defaultdict(dict)
    for i, x in enumerate(data):
        initialpoints[i]["p"], initialpoints[i]["v"], initialpoints[i]["a"] = [
            tuple(map(int, arr.split(","))) for arr in x
        ]

    pts = deepcopy(initialpoints)
    ticks = 1000  # Assume this is enough to get to "long term"
    for tick in range(ticks):
        for p in pts:
            pts[p]["v"] = tuple([pts[p]["v"][i] + pts[p]["a"][i] for i in range(3)])
            pts[p]["p"] = tuple([pts[p]["p"][i] + pts[p]["v"][i] for i in range(3)])

    print(
        "Part A:", min(pts, key=lambda p: sum([abs(pts[p]["p"][x]) for x in range(3)]))
    )

    pts = deepcopy(initialpoints)
    ticks = 1000  # Assume this is enough to get to "long term"
    for tick in range(ticks):
        posmap = defaultdict(list)
        for p in pts:
            pts[p]["v"] = tuple([pts[p]["v"][i] + pts[p]["a"][i] for i in range(3)])
            pts[p]["p"] = tuple([pts[p]["p"][i] + pts[p]["v"][i] for i in range(3)])

            posmap[pts[p]["p"]].append(p)

        # Collisions
        for ps in posmap:
            if len(posmap[ps]) > 1:
                for p in posmap[ps]:
                    del pts[p]

    print("Part B:", len(pts))
