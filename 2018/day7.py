if __name__ == "__main__":
    f = open("day7.in", "r")
    data = [(y[1], y[-3]) for y in [x.split() for x in f.read().splitlines()]]
    f.close()

    labels = set([x[0] for x in data]).union([x[1] for x in data])

    finishedtasks = set()
    order = ""
    while not len(finishedtasks) == len(labels):
        notallowedcands = set()
        for x in data:
            requiredtask, unlockedtask = x[0], x[1]
            if not requiredtask in finishedtasks:
                notallowedcands.add(unlockedtask)

        sortedcands = sorted(
            labels.difference(finishedtasks).difference(notallowedcands)
        )

        order += sortedcands[0]
        finishedtasks.add(sortedcands[0])
    print("Part A:", order)

    finishedtasks = set()
    iterations = 0
    maxworkers = 5
    inprogresscands = set()  # type (tag,remaining)[]
    while not len(finishedtasks) == len(labels):
        for i in range(maxworkers):
            if len(inprogresscands) == maxworkers:
                break

            notallowedcands = set([x[0] for x in inprogresscands])
            for x in data:
                requiredtask, unlockedtask = x[0], x[1]
                if not requiredtask in finishedtasks:
                    notallowedcands.add(unlockedtask)

            sortedcands = sorted(
                labels.difference(finishedtasks.union(notallowedcands))
            )

            if len(sortedcands) == 0:
                break
            inprogresscands.add((sortedcands[0], ord(sortedcands[0]) - 4))
        iterations += 1
        stillinprogress = set()
        for x in inprogresscands:
            if x[1] - 1 == 0:
                finishedtasks.add(x[0])
            else:
                stillinprogress.add((x[0], x[1] - 1))
        inprogresscands = stillinprogress

    print("Part B:", iterations)
