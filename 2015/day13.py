from itertools import permutations

if __name__ == "__main__":
    f = open("day13.in", "r")
    data = [
        row.replace(" would", "")
        .replace(" happiness units by sitting next to", "")
        .replace(".", "")
        .split(" ")
        for row in f.read().splitlines()
    ]
    f.close()

    preferences = {}
    for row in data:
        person = row[0]
        positive = True if row[1] == "gain" else False
        value = int(row[2])
        target = row[3]
        if not person in preferences:
            preferences[person] = {}
        preferences[person][target] = value if positive else -value

    persons = set()
    for row in data:
        persons.add(row[0])

    perms = permutations(persons)

    scores = {
        sum(
            [
                preferences[a][b] + preferences[b][a]
                for a, b in zip(perm, (perm[1:] + (perm[0],)))
            ]
        )
        for perm in perms
    }

    print("Part A:", max(scores))

    preferences["Me"] = {}
    for person in persons:
        preferences["Me"][person] = 0
        preferences[person]["Me"] = 0
    persons.add("Me")

    perms = permutations(persons)

    scores = {
        sum(
            [
                preferences[a][b] + preferences[b][a]
                for a, b in zip(perm, (perm[1:] + (perm[0],)))
            ]
        )
        for perm in perms
    }

    print("Part B:", max(scores))
