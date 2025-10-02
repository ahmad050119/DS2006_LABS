from dice import rollD6, rollD4, rollD8, rollD12, rollD20, rollD100, rollD2
import copy
print("🎲 Welcome to Battle of Dices! 🎲")
# Variables to keep track of the score:

# dice options to make the "level selector" easiser to code
dice_options = {
   
   "D2": rollD2,
   "D4": rollD4,
   "D6": rollD6,
   "D8": rollD8,
   "D12": rollD12,
}

# player dic to store information
player_info = {
   
   "name": "",
   "email": "",
   "country": "",
   "lucky_die": None, #add the chosen lucky dice to the player info
   "lucky_die_name": "", # this is for display of the dice name
   "wins": 0,
   "rolls": []
}

# list to store each players dic
players = []

# input to determine number of players
try: # try cause i dont wanna see error mesages
  number_of_players = int(input("how many players are playing? "))
except ValueError:
  print("try a number")

#for loop to get player names and initialize their win counts
for i in range(number_of_players):

    # making a deep copy of the dic template for the player
    player = copy.deepcopy(player_info)

# get input about each player and add them to the dic in seperate lists
    player["name"] = input (f"enter the name of player {i+1}: ")
    player["email"] = input(f"enter the email for player {i+1}: ")
    player["country"] = input(f"enter the country of player {i+1}: ")

    try: # try cause i dont wanna see error messages
      lucky_number = int(input("On a scale of 1 to 6, how lucky are you feeling today? "))
    except ValueError:
       
       print ("try a number")
       
       # the so called "level selector"
    match lucky_number:
            case 1:
                player["lucky_die"] = rollD2
                player["lucky_die_name"] = "D2"
                print("you get to roll a D2, negativity results in more negativity be positive next time :)")
            case 2:
                player["lucky_die"] = rollD4    
                player["lucky_die_name"] = "D4"
                print ("mmm, not feeling lucky huh? you get to roll a D4, remebmber YOU make your own luck")
            case 3:
                player["lucky_die"] = rollD6
                player["lucky_die_name"] = "D6"
                print("not bad thats the safe option, you get to roll a D6")
            case 4:
                player["lucky_die"] = rollD8
                player["lucky_die_name"] = "D8"
                print("love the confiendince you get to roll a D8")
            case 5:
                player["lucky_die"] = rollD12
                player["lucky_die_name"] = "D12"
                print("GOOD CHOICE, you get to roll a D12. stay positive")
            case _:
                print("nope, enter a number between 1 and 6.")
   
    players.append(player) 
   
# an outer loop to allow replaying the game
gameover = False
rounds_played = 0
#the number of wins needed to win the game
wining_score = 3
while gameover is False: 
    
    rounds_played += 1
    print(f"\n this is round {rounds_played}")

    enter= input("press enter to conintiue")

    # list to store dice rolls for each player in the current round
    current_rolls = []
    round_totals = []

    # for loop to get each player's roll
    for each_player in players: 
      roll1 = rollD6()
      roll2 = each_player["lucky_die"]()
      total_rolls = roll1 + roll2
      each_player["rolls"].append((roll1,roll2, total_rolls))
      round_totals.append(total_rolls)
      print(f"player {each_player['name']}, rolled: {roll1}, {roll2} for a total of {total_rolls}")

  # enter to keep going 
    input("\nPress ENTER to continue...")

  # determine the highest roll
    max_roll = max(round_totals)

    # list to store winners of the round
    round_winners = []

    #check for who had the highest roll
    for each_player in players:
        if each_player["rolls"][-1][2] == max_roll:
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
        f"lucky dice: {each_player["lucky_dice_name"]}\n"
        f"* E-mail: {each_player["email"]}\n"
        f"* Country: {each_player["country"]}\n"
        f"* Wins: {each_player["wins"]}\n\n"

     )
  file.write ("\n Game rounds: \n")

  # round history
  for r in range(rounds_played):
     file.write(f"\n Round {r+1}")

# new improved file log
     for each_player in players:
        roll1, roll2, total = each_player["rolls"][r]
        file.write(
            f"{each_player['name']} rolled {roll1}, "
            f"and a {roll2} for a total of: {total}\n"
        )

    # write the full round info
     file.write("\n")

  print ("\n game over! Results saved successfully.")
        
        
        
  

