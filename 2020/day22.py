if __name__ == "__main__":
    f = open("day22Input.txt", "r")
    data = [
        [int(y) for y in x.splitlines()[1:]] for x in f.read().strip().split("\n\n")
    ]
    f.close()
    player1 = data[0].copy()
    player2 = data[1].copy()

    def solvegame(player1, player2):
        while len(player1) > 0 and len(player2) > 0:
            p1 = player1.pop(0)
            p2 = player2.pop(0)
            if p1 > p2:
                player1.extend([p1, p2])
            elif p2 >= p1:
                player2.extend([p2, p1])
        if len(player1) > 0:
            return player1
        return player2

    winner = solvegame(player1.copy(), player2.copy())
    print("Part A:", sum([int(x) * (len(winner) - i) for i, x in enumerate(winner)]))

    # Part B
    def solveRecursiveGame(player1, player2):
        rounds = set()
        while len(player1) > 0 and len(player2) > 0:
            nextTuple = (tuple(player1), tuple(player2))
            if nextTuple in rounds:
                return player1, "player1"
            rounds.add(nextTuple)

            a = player1.pop(0)
            b = player2.pop(0)

            if len(player1) >= a and len(player2) >= b:
                winnerarr, winner = solveRecursiveGame(player1[:a], player2[:b])
                if winner == "player1":
                    player1.extend([a, b])
                else:
                    player2.extend([b, a])
            elif a >= b:
                player1.extend([a, b])
            else:
                player2.extend([b, a])

        if len(player1) > len(player2):
            return player1, "player1"
        else:
            return player2, "player2"

    winnerarr, winner = solveRecursiveGame(player1.copy(), player2.copy())
    print(
        "Part B:", sum([int(x) * (len(winnerarr) - i) for i, x in enumerate(winnerarr)])
    )
