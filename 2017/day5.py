if __name__ == "__main__":
    f = open("day5.in", "r")
    data = [int(x) for x in f.read().splitlines()]
    f.close()

    i = 0
    steps = 0
    nums = data.copy()
    while i < len(nums):
        steps += 1
        togo = i + nums[i]
        nums[i] += 1
        i = togo

    print("Part A:", steps)

    nums = data.copy()
    i = 0
    steps = 0
    while i < len(nums):
        steps += 1
        togo = i + nums[i]
        if nums[i] >= 3:
            nums[i] -= 1
        else:
            nums[i] += 1
        i = togo

    print("Part B:", steps)
