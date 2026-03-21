from wordle_solution import solution, secret_message

truthyness = True


def wordle(word, solution):
    if not len(word) == 5:
        return "ERROR! word must be 5 letters long"

    word = word.lower()
    solution = solution.lower()

    if word == solution:
        global truthyness
        truthyness = False
        return secret_message
    else:
        store = []
        for position, letter in enumerate(word):
            if letter == solution[position]:
                print(letter, end=" ")

            elif letter in solution:
                print("_", end=" ")
                store += letter

            else:
                print("_", end=" ")
    print("\n", store, "is elsewhere")

    return "You've got this. Try again, Bubz!"


while truthyness == True:
    word = input("Enter a 5 letter word: ")
    print(wordle(word, solution))
