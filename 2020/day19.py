import re

if __name__ == "__main__":
    f = open("day19Input.txt", "r")
    data = f.read().split("\n\n")
    f.close()

    rules = [[y.strip() for y in x.split(":")] for x in data[0].splitlines()]
    messages = data[1].splitlines()

    rulemap = {x[0]: x[1] for x in rules}
    rulemap = {x: rulemap[x].replace(" | ", "|").replace(" ", "&") for x in rulemap}

    rulemap = {
        x: [y.split("&") for y in rulemap[x].split("|")]
        if not (rulemap[x] == '"a"' or rulemap[x] == '"b"')
        else rulemap[x][1:-1]
        for x in rulemap
    }

    def resolve(rule, rulemap):
        if rulemap[rule] == "a" or rulemap[rule] == "b":
            return rulemap[rule]
        else:
            optionsout = []
            for option in rulemap[rule]:
                resolved = ""
                for rule in option:
                    resolved = resolved + "(" + "".join(resolve(rule, rulemap)) + ")"
                optionsout.append(resolved)
            return "|".join(optionsout)

    pattern = resolve("0", rulemap)
    count = 0
    for message in messages:
        if not re.fullmatch(pattern, message) == None:
            count += 1
    print("Part A:", count)

    # Part B
    rulemap["8"] = [["42"]]
    rulemap["11"] = [["42", "31"]]

    # HACK: guess copies and try -> When no. of matched dont seem to increase, you have your ans
    copies = 20
    for i in range(1, copies):
        toappend8 = ["42"]
        toappend11 = ["42", "31"]
        for j in range(0, i):
            toappend8.append("42")
            toappend11.insert(0, "42")
            toappend11.insert(-1, "31")
        rulemap["8"].append(toappend8)
        rulemap["11"].append(toappend11)

    pattern = resolve("0", rulemap)
    count = 0
    for message in messages:
        if not re.fullmatch(pattern, message) == None:
            count += 1
    print("Part B:", count)
