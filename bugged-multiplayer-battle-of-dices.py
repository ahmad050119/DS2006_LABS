from dice import rollD6, rollD4, rollD8, rollD12, rollD20, rollD100
import copy
print("🎲 Welcome to Battle of Dices! 🎲")

#my_nested_list = []
# Variables to keep track of the score:

#the number of wins needed to win the game
wining_score = 3
#array to store player names
#player_names = []
#array to store the amount of wins
#player_wins = []

# player dic to store information
player_info = {
   
   "name": "",
   "email": "",
   "country": "",
   "wins": 0,
   "rolls": []
}

# list to store each players dic
players = []

# input to determine number of players
number_of_players = int(input("how many players are playing?"))

#for loop to get player names and initialize their win counts
for i in range(number_of_players):

    # making a deep copy of the dic template for the player
    player = player_info.copy()

# get input about each player and add them to the dic in seperate lists
    player["name"] = input (f"enter the name of player {i+1} ")
    player["email"] = input(f"enter the email for player {i+1} ")
    player["country"] = input(f"enter the country of player {i+1} ")
   
    players.append(player) 

# initialize score and wins

#for i in range(number_of_players):
 #   player_wins.append(0)
    

# initialize player rolls as empty lists
#for i in range(number_of_players):
    #adds an empty list for each player
 #   my_nested_list.append([])


# an outer loop to allow replaying the game
gameover = False
rounds_played = 0
while gameover is False: 
    
    rounds_played += 1
    print(f"\n this is round {rounds_played}")

    enter= input("press enter to conintiue")

    # list to store dice rolls for each player in the current round
    current_rolls = []

    # for loop to get each player's roll
    for each_player in players: 
      roll = rollD6()
      current_rolls.append(roll)
      #player_rolls_history.append(roll)
      each_player['rolls'].append(roll)
      print(f"player {each_player['name']}, rolled: {roll}")

  # enter to keep going 
    input("\nPress ENTER to continue...")

  # determine the highest roll
    max_roll = max(current_rolls)

    # list to store winners of the round
    round_winners = []

    #check for who had the highest roll
    for each_player in players:
        if (each_player["rolls"][-1] == max_roll):
            each_player["wins"] += 1
            round_winners.append(each_player['name'])
            
  
    print(f"winners this round are: {round_winners}!")

    # check if any player has reached the winning score
    for each_player in players:
      if (each_player["wins"] >= wining_score):
        print(f"\n {each_player['name']} wins the game with {each_player['wins']} wins!")
        gameover = True
        break
    if gameover is False:
      
      print(f"the battle continues to round {rounds_played}!")
      print(" --.....................--  ")



# option to save log history to a text file
filename = input("Enter a filename to save the log history: ")
with open(filename, 'w') as file:
  #player information
  file.write("player information: \n")

  for each_player in players:
     file.write(
        f"Name: {each_player["name"]}\n"
        f"* E-mail: {each_player["email"]}\n"
        f"* Country: {each_player["country"]}\n"
        f"* Wins: {each_player["wins"]}\n\n"

     )
  file.write ("\n Game rounds: \n")

  # round history
  for r in range(rounds_played):
     #start with empty text 
     rolls_str = ""

     # go through each player and build string step by step
     for i, each_player in enumerate(players):
        rolls_str += f"{each_player['name']} rolled {each_player['rolls'][r]}"

        # add comma and space
        if i < len(players) - 1: 
           rolls_str += ", "

    # write the full round info
     file.write(f"Round {r+1}: \n {rolls_str}\n")

  print ("\n game over! Results saved successfully.")
        
        
        
  

