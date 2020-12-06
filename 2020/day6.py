from functools import reduce

if __name__ == "__main__":
    f = open("day6Input.txt", "r")
    data = [x.replace("\n", " ").split(" ") for x in f.read().strip().split("\n\n")]
    f.close()

    answerCount = 0
    for group in data:
        groupAnswers = []
        for person in group:
            for char in person:
                if char not in groupAnswers:
                    groupAnswers.append(char)
        answerCount += len(groupAnswers)

    print("(A), All: ", answerCount)

    commonAnswerCount = 0
    for group in data:
        groupAnswers = group[0]
        for person in group:
            newAnswers = ""
            for answer in person:
                if answer in groupAnswers:
                    newAnswers = newAnswers + answer
            groupAnswers = newAnswers
        commonAnswerCount += len(groupAnswers)

    print("(B), Common: ", commonAnswerCount)
