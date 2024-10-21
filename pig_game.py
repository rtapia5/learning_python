""" from 'Tech with Tim' video https://www.youtube.com/watch?v=21FnnGKSRZo """

import random

#player roll dice(some type of random generator)

#ask player wether to continue or stop

#need some roll function
def roll():
    roll = random.randint(1,6)

    return roll

#value = roll()
#print(value)



while True: # checking if the imput is within the desired number of players (2 - 4) in this case
    players = input("Enter the number of players (2 - 4): ") #storing player input into variable "players"
    if players.isdigit(): 
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")
        
max_score = 50
player_scores = [0 for i in range(players)]

while max(player_scores) < max_score:

    for player_idx in range(players):
        print("\nPlayer number ", player_idx + 1, "turn has just started!\n")
        print("Your total score is: ", player_scores[player_idx], "\n")
        current_score = 0

        while True:

            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a: ", value)

            print("Your score is: ", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1,
      "is the winner with a score of:", max_score)