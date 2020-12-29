def transformn(num, n):
    def transform(num):
        output = ""
        i = 0
        count = 1
        while i < len(num):
            if i == len(num) - 1:
                output += str(count)
                output += num[i]
            elif num[i] == num[i + 1]:
                count += 1
            else:
                output += str(count)
                output += num[i]
                count = 1
            i += 1
        return output

    curr = num
    for i in range(n):
        curr = transform(curr)
    return curr


if __name__ == "__main__":
    f = open("day10.in", "r")
    data = f.read().splitlines()[0]
    f.close()

    print("Part A:", len(transformn(data, 40)))

    print("Part B:", len(transformn(data, 50)))
