f = open("day10Input.txt", "r")
data = set([int(i) for i in f.read().splitlines()])
f.close()

diffmap = {1: 0, 2: 0, 3: 0}
last = 0
for item in data:
    diffmap[item - last] += 1
    last = item

print(
    "Part A",
    # Final one always three higher than higest in dataset
    diffmap[1] * (diffmap[3] + 1),
)


def paths(item, data):
    cache = {0: 1}
    for i in sorted(data):
        if i > item:
            break
        cache[i] = 0
        for jumpLength in [1, 2, 3]:
            if i - jumpLength in data or (i - jumpLength) == 0:
                cache[i] = cache[i] + cache[i - jumpLength]

    return cache[item]


print("Part B: ", paths(max(data), data))
