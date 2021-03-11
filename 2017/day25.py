if __name__ == "__main__":
    # Write data from input manually
    iterations = 12172063

    stateTransition = {
        0: {"A": "B", "B": "A", "C": "D", "D": "B", "E": "C", "F": "E"},
        1: {"A": "C", "B": "D", "C": "C", "D": "E", "E": "F", "F": "A"},
    }

    slotTransition = {
        0: {"A": 1, "B": -1, "C": 1, "D": -1, "E": 1, "F": -1},
        1: {"A": -1, "B": -1, "C": 1, "D": 1, "E": -1, "F": 1},
    }

    getValue = {
        0: {"A": 1, "B": 1, "C": 1, "D": 0, "E": 1, "F": 1},
        1: {"A": 0, "B": 1, "C": 0, "D": 0, "E": 1, "F": 1},
    }

    step = 0
    slot = iterations
    state = "A"
    tape = [0 for i in range(2 * iterations)]

    while step < iterations:
        curr = tape[slot]
        value = getValue[curr][state]
        tape[slot] = value
        slot += slotTransition[curr][state]
        state = stateTransition[curr][state]
        step += 1

    print("Part A:", tape.count(1))
