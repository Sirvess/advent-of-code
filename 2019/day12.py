from copy import deepcopy

if __name__ == "__main__":
    f = open("day12.in", "r")
    data = [
        x.replace("<", "").replace(">", "").replace("=", "").replace(",", "").split()
        for x in f.read().splitlines()
    ]
    data = [[int(y[1:]) for y in x] for x in data]
    f.close()

    planets = {i: {} for i in range(len(data))}
    for p in planets:
        planets[p]["pos"] = data[p]
        planets[p]["vel"] = [0, 0, 0]

    steps = 1000
    for i in range(steps):
        # Apply gravity
        oldplanets = deepcopy(planets)
        for p in planets:
            dgrav = [0, 0, 0]
            for k in planets:
                if k == p:
                    continue
                for z in range(3):
                    if oldplanets[p]["pos"][z] < oldplanets[k]["pos"][z]:
                        dgrav[z] += 1
                    elif oldplanets[p]["pos"][z] > oldplanets[k]["pos"][z]:
                        dgrav[z] -= 1
            for z in range(3):
                planets[p]["vel"][z] += dgrav[z]

        # Apply velocity
        for p in planets:
            for z in range(3):
                planets[p]["pos"][z] += planets[p]["vel"][z]

    energy = 0
    for p in planets:
        poten = sum([abs(x) for x in planets[p]["pos"]])
        kinen = sum([abs(x) for x in planets[p]["vel"]])
        energy += poten * kinen
    print("Part A:", energy)
