import re


def countValidPasswords(data, rule):
    if(rule == "count"):
        return len(
            list(
                filter(
                    lambda node: len(
                        re.findall(
                            node["char"],
                            node["pw"])) in range(
                        node["a"],
                        node["b"] +
                        1),
                    data)))
    elif(rule == "pos"):
        return len(list(filter(lambda node: [node["pw"][node["a"] - 1] == node["char"],
                                             node["pw"][node["b"] - 1] == node["char"]].count(True) == 1,
                               filter(lambda node: len(node["pw"]) >= node["b"] - 1,
                                      data))))
    return "Invalid rule."


def formatInput(data):
    return map(lambda x: {"a": int(x[0]),
                          "b": int(x[1]),
                          "char": x[2][:-1],
                          "pw": x[3]},
               map(lambda node: re.split("[\n -]",
                                         node,
                                         maxsplit=4),
                   inData))


if __name__ == "__main__":
    f = open("day2Input.txt", "r")
    inData = f.readlines()
    f.close()

    # Results
    print(
        "Valid according to count: ",
        countValidPasswords(
            formatInput(inData),
            "count"))
    print(
        "Valid according to position: ",
        countValidPasswords(
            formatInput(inData),
            "pos"))
