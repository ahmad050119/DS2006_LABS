from dice import rollD6, rollD4, rollD8, rollD12, rollD20, rollD100
print("🎲 Welcome to Battle of Dices! 🎲")

my_nested_list = []
# Variables to keep track of the score:

#the number of wins needed to win the game
wining_score = 3
#array to store player names
player_names = []
#array to store the amount of wins
player_wins = []
# input to determine number of players
number_of_players = int(input("how many players are playing?"))
#for loop to get player names and initialize their win counts
for i in range(number_of_players):
    name = input(f"Enter the name of player {i+1}: ")
    player_names.append(name)

# initialize score and wins

for i in range(number_of_players):
    player_wins.append(0)
    

# initialize player rolls as empty lists
for i in range(number_of_players):
    #adds an empty list for each player
    my_nested_list.append([])


# an outer loop to allow replaying the game
gameover = False

while gameover is False:
    player_rolls_history = []
    rounds_played = 1
    print(f"round {rounds_played}")
    # list to store dice rolls for each player in the current round
    current_rolls = []

    # for loop to get each player's roll
    for i in range(number_of_players): 
      roll = rollD6()
      current_rolls.append(roll)
      player_rolls_history.append(roll)
      print(f"{player_names[i]} rolled: {roll}")

  # enter to keep going 
    input("\nPress ENTER to continue...")

  # determine the highest roll
    max_roll = max(current_rolls)

    # list to store winners of the round
    round_winners = []

    #check for who had the highest roll
    for j in range(len(current_rolls)):
        if current_rolls[j] == max_roll:
            round_winners.append(player_names[j])
            player_wins[j] += 1
  
    print(f"winners this round are: {round_winners}!")

    # check if any player has reached the winning score
    for k in range(len(player_wins)):
      if player_wins[k] >= wining_score:
        print(f"\n {player_names[k]} wins the game with {player_wins[k]} wins!")
        gameover = True
        break
    if gameover is False:
      rounds_played += 1
      print(f"the battle continues to round {rounds_played}!")
      print(" --.....................--  ")

# option to save log history to a text file
filename = input("Enter a filename to save the log history: ")
with open(filename, 'w') as file:
  for rounds_played in range(len(player_rolls_history)):
    file.write(f"Round {rounds_played+1}: ")
    rolls_str = ""  # to make it start with an empty string
    for player in range(number_of_players):
      rolls_str += f"{player_names[player]} rolled {player_rolls_history[player]} "
      if player < number_of_players - 1:  # to add a comma between rolls except for the last one
        rolls_str += ", "
    print(f"saving to file: {rolls_str}")
    file.write(rolls_str + "\n")

