from dice import rollD6, rollD4, rollD8, rollD12, rollD20, rollD100
print("🎲 Welcome to Battle of Dices! 🎲")

while True:

    player1_wins = 0
    player2_wins = 0

    p1_total = 0
    p2_total = 0
    list_of_player1_roll =[]
    list_of_player2_roll =[]
    player1_name = input(f"please enter your name: ")
    player2_name = input(f"please enter your name: ")
    Level = input(f"Welcome {player1_name}, well then from 1 to 3 how lucky are you feeling today? ")
    

    #this is supposed to work as a difficulty level selector based on the the luck level
    #if Level == "3":
     #   print("wow, such confidence!, you get to roll an additional D20")
      #  player1_roll = rollD20()
       # player1_roll2 = rollD6()
    #elif Level == "2":
     #   print("not bad, you get to roll a D6")
      #  player1_roll = rollD6()
       # player1_roll2 = rollD6()

    #elif Level == "1":
     #   print("hmm, negativity breeds more negativity, you get to roll an additional D4")
      #  player1_roll = rollD4()  
       # player1_roll2 = rollD6() 
    #else:
     #   print(Level,"?", "Thats invalid input, you get to roll an additional D1")
      #  player1_roll = 1
       # player1_roll2 = rollD6()


# Variables to keep track of the score:
    while player1_wins < 3 and player2_wins < 3:
      player2_roll = rollD6()
      player2_roll2 = rollD6()

        #this is supposed to work as a difficulty level selector based on the the luck level

   
      player1_roll = rollD20()
      player1_roll2 = rollD6()
     
     

      input("\nPress ENTER to roll the dice...")

      #sum of rolls
      p1_sumRoll = player1_roll + player1_roll2
      p2_sumRoll = player2_roll + player2_roll2
      

      #this is just for decoration 
      print(" --.....................--  ")

      print(f"\nthis is round ", rounds_played)

      #roll the dices
      print(f"{player1_name} rolled: ", player1_roll, " and ", player1_roll2, "with a total of ", p1_sumRoll)
      #list of roll history for player 1
      list_of_player1_roll.append((player1_roll,player1_roll2))
     
      
      
      print("Player 2 rolled: ", player2_roll, " and ", player2_roll2, "with a total of ", p2_sumRoll)
      #list of roll history for player 2
      list_of_player2_roll.append((player2_roll,player2_roll2))
    
      

      input("\nPress ENTER to continue...")

 # So far so good right? But how to check who got the highest roll?

      if p1_sumRoll > p2_sumRoll:
       player1_wins +=1
       print(f"{player1_name} wins this round!")
       print("Because ", p1_sumRoll," is greater than ", p2_sumRoll)
       
      elif p1_sumRoll == p2_sumRoll:
       print("Amaaazzinng! This round has a tie!")

      else:
       player2_wins += 1
       print("Player 2 wins this round!")
       print("Because ", p2_sumRoll," is greater than ", p1_sumRoll)

 # We can print the game score:
      print(f"game score is {player1_name}.", player1_wins,"points", "vs"," Player2. ", player2_wins,"Points")
      rounds_played += 1

 # Now we need to check if either player won.
      if player1_wins == 3:
       print(f"{player1_name} winner, time for your chicken dinner!")
       print, ("total rounds played: ", rounds_played -1)
       print(" --.....................--  ")
      elif player2_wins == 3:
       print("Player 2 winner, time for your chicken dinner!")
       print, ("total rounds played: ", rounds_played -1)
       print(" --.....................--  ")
      else:
       print("this battle is at stalemate, the chiken is still cooking!!")
       #this is just for decoration 
       print(" --.....................--  ")

# printing log history of rolls for both players
    print("Here is the log of the battle for Player 1:")   
    for each_roll, (r1, r2) in enumerate (list_of_player1_roll, 1):    
      print(f"Round {each_roll}: {r1} and {r2}")

    print("Here is the log of the battle for Player 2:")   
    for each_roll,(r1, r2) in enumerate (list_of_player2_roll, 1):    
      print(f"Round {each_roll}: {r1} and {r2}")

# option to save log history to a text file
    filename = input ( "Enter a filename to save the log history:")
    with open (filename, 'w') as file:
      for i in range(len(list_of_player1_roll)):
        file.write(f"Round {i+1}: Player 1 rolled {list_of_player1_roll[i]}, Player 2 rolled {list_of_player2_roll[i]}\n")
    
# ask if they want to play again once loop is done
    play_again = input("do you want to play again? y/n: ")
    if play_again != "y":                                   
       print("thanks for playing!.")
     #command used to break the outer loop and exit the game
       break