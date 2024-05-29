# Write your solution here
from random import choice

def roll(die: str):  
    A = [3, 3, 3, 3, 3, 6]
    B = [2, 2, 2, 5, 5, 5]
    C = [1, 4, 4, 4, 4, 4]
    dices = {"A": A, "B": B, "C": C}
 
    return choice(dices[die])

def play(die1: str, die2: str, times: int):
    A = [3, 3, 3, 3, 3, 6]
    B = [2, 2, 2, 5, 5, 5]
    C = [1, 4, 4, 4, 4, 4]
    dices = {"A": A, "B": B, "C": C}

    p1 = 0
    p2 = 0
    tie = 0
    for i in range(times):
        player_1 = choice(dices[die1])
        player_2 = choice(dices[die2])
        if int(player_1) > int(player_2):
            p1 += 1
        elif int(player_1) < int(player_2):
            p2 += 1
        else:
            tie += 1
    return (p1, p2, tie)

if __name__ == "__main__":
    
    for i in range(20):
        print(roll("A"), " ", end="")
    print()
    for i in range(20):
        print(roll("B"), " ", end="")
    print()
    for i in range(20):
        print(roll("C"), " ", end="")
    print()
    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)