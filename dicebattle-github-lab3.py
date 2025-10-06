# Battle of Dices is going to be an amazing 2 player game, 
# where two players face each other using only their sheer luck! 
# 
# The rules are:
# 
# Each player throws one D6.
# The player with the highest roll wins the round.  
# The first player to win 3 times is the winner.
#
# Our main task today is to implement the code necessary to bring this
# amazing game alive!

from dice import rollD6, rollD4, rollD8, rollD12, rollD20, rollD100
print("🎲 Welcome to Battle of Dices! 🎲")


# an outer loop to allow replaying the game
while True:
    # Variables to keep track of the score:
    player1_wins = 0
    player2_wins = 0
    rounds_played = 1
    player1_name = input(f"please enter your name: ")
    Level = input(f"Welcome {player1_name}, well then from 1 to 3 how lucky are you feeling today? ")
    player2_roll = rollD6()
    player2_roll2 = rollD6()
    


    #this is supposed to work as a difficulty level selector based on the the luck level
    if Level == "3":
        print("wow, such confidence!, you get to roll an additional D20")
        player1_roll = rollD20()
        player1_roll2 = rollD6()
    elif Level == "2":
        print("not bad, you get to roll a D6")
        player1_roll = rollD6()
        player1_roll2 = rollD6()

    elif Level == "1":
        print("hmm, negativity breeds more negativity, you get to roll an additional D4")
        player1_roll = rollD4()  
        player1_roll2 = rollD6() 
    else:
        print(Level,"?", "Thats invalid input, you get to roll an additional D1")
        player1_roll = 1
        player1_roll2 = rollD6()


# Variables to keep track of the score:
    while player1_wins < 3 and player2_wins < 3:
     

      input("\nPress ENTER to roll the dice...")

      #sum of rolls
      p1_sumRoll = player1_roll + player1_roll2
      p2_sumRoll = player2_roll + player2_roll2

      #this is just for decoration 
      print(" --.....................--  ")

      print(f"\nthis is round ", rounds_played)

      #roll the dices
      print(f"{player1_name} rolled: ", player1_roll, " and ", player1_roll2, "with a total of ", p1_sumRoll)
      
      print("Player 2 rolled: ", player2_roll, " and ", player2_roll2, "with a total of ", p2_sumRoll)

      input("\nPress ENTER to continue...")

 # So far so good right? But how to check who got the highest roll?
      if p2_sumRoll > p2_sumRoll:
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

# ask if they want to play again once loop is done
    play_again = input("do you want to play again? y/n: ")
    if play_again != "y":
       print("thanks for playing!.")
     #command used to break the outer loop and exit the game
       break
   

     
      



   






