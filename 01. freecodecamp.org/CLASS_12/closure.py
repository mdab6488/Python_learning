# Closure is a function having access to the scope of its parent function after the parent function has returned.


def paraent_function(person, coins):
    # coins = 3

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print(f"{person} has {coins} coins left.")
        elif coins == 1:
            print(f"{person} has {coins} coins left.")
        else:
            print(f"{person} is out of coins.")

    return play_game


tommay = paraent_function("Tommay", 3)
jenny = paraent_function("jenny", 5)

tommay()
tommay()

jenny()

tommay()
