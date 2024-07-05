# Closure is a function having access to the scope of its parent function after the parent function has returned.

def parent_function(person, coins):
    # coins = 3

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left.")
        else:
            print("\n" + person + " is out of coins.")

    # return play_game()
    return play_game

# Here the parent_function returns the play_game function, which is stored in the variables tommy and jenny.
# The play_game function has access to the coins variable from the parent_function, even after the parent_function has returned. 


tommy = parent_function("Tommy", 3)
jenny = parent_function("Jenny", 5)

tommy()
tommy()

jenny()

tommy()