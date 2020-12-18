def resolveAddsAndMultsB(numarr):
    if isinstance(numarr, str):
        return int(numarr)

    curr = numarr
    for op in ["+", "*"]:
        r = 0
        while op in curr:
            r = curr.index(op)
            toadd = eval(curr[r - 1] + op + curr[r + 1])
            for i in range(0, 3):
                curr.pop(r - 1)
            if len(curr) <= r - 1:
                curr.append(str(toadd))
            else:
                curr.insert(r - 1, str(toadd))
    return curr[0]


def resolveAddsAndMultsA(numarr):
    acc = int(numarr[0])
    for i, x in enumerate(numarr):
        if x == "+":
            acc += int(numarr[i + 1])
        elif x == "*":
            acc *= int(numarr[i + 1])
    return acc


def reduceParens(nums, mode):
    if not "(" in nums:
        if mode == "A":
            return resolveAddsAndMultsA(nums)
        elif mode == "B":
            return resolveAddsAndMultsB(nums)
    else:
        l = nums.index("(")
        r = l

        openparens = 1
        while openparens > 0:
            r += 1
            if nums[r] == "(":
                openparens += 1
            elif nums[r] == ")":
                openparens -= 1
        closingparen = r

        reducedparen = reduceParens(nums[l + 1 : closingparen], mode)

        restarr = [x for i, x in enumerate(nums) if i not in range(l, closingparen + 1)]
        restarr.insert(l, reducedparen)
        return reduceParens(restarr, mode)


if __name__ == "__main__":
    f = open("day18Input.txt", "r")
    data = [
        x.replace("(", "( ").replace(")", " )").split(" ")
        for x in f.read().splitlines()
    ]
    f.close()

    outsum = 0
    for expr in data:
        curr = expr
        while not isinstance(curr, int):
            curr = reduceParens(curr, "A")
        outsum += curr
    print("Part A", outsum)

    outsum = 0
    for expr in data:
        curr = expr
        while not isinstance(curr, int):
            curr = reduceParens(curr, "B")
        outsum += curr
    print("Part B", outsum)
