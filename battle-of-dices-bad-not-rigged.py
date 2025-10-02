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

import random

print("🎲 Welcome to Battle of Dices! 🎲")

# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0

# Round 1
input("\nPress ENTER to roll the dice...")

player1_roll = random.randint(1, 6)
player1_roll2 = random.randint(1, 6)
player1_roll3 = random.randint(1, 6)
player1_roll4 = random.randint(1, 6)
player1_roll5 = random.randint(1, 6)
player1_roll6 = random.randint(1, 6)
player1_roll7 = random.randint(1, 6)
print("Player 1 rolled: ", player1_roll)


player2_roll = random.randint(1, 6)
player2_roll2 = random.randint(1, 6)
player2_roll3 = random.randint(1, 6)
player2_roll4 = random.randint(1, 6)
player2_roll5 = random.randint(1, 6)
player2_roll6 = random.randint(1, 6)
player2_roll7 = random.randint(1, 6)
print("Player 2 rolled: ", player2_roll)


input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll," is greater than ", player2_roll)
elif player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll," is greater than ", player1_roll)

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 winner, time for your chicken dinner! ")
elif player2_wins == 3:
    print("Player 2 winner, time for your chicken dinner! ")
else:
    print("this battle is at stalemate, pray to god that you win today!")

    input("\nPress ENTER to roll the dice...")

# round 2
player1_roll2 = random.randint(1, 6)
print("Player 1 rolled: ", player1_roll2)


player2_roll2 = random.randint(1, 6)
print("Player 2 rolled: ", player2_roll2)


input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll2 > player2_roll2:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll2," is greater than ", player2_roll2)
elif player1_roll2 == player2_roll2:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll2," is greater than ", player1_roll2)

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 winner, time for your chicken dinner! ")
elif player2_wins == 3:
    print("Player 2 winner, time for your chicken dinner! ")
else:
    print("this battle is at stalemate, pray to god that you win today!")

    input("\nPress ENTER to roll the dice...")

player1_roll3 = random.randint(1, 6)
print("Player 1 rolled: ", player1_roll3)


player2_roll3 = random.randint(1, 6)
print("Player 2 rolled: ", player2_roll3)


input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll3 > player2_roll3:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll3," is greater than ", player2_roll3)
elif player1_roll3 == player2_roll3:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll3," is greater than ", player1_roll3)

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 winner, time for your chicken dinner! ")
elif player2_wins == 3:
    print("Player 2 winner, time for your chicken dinner! ")
else:
    print("this battle is at stalemate, pray to god that you win today!")

    input("\nPress ENTER to roll the dice...")
# round 4
player1_roll4 = random.randint(1, 6)
print("Player 1 rolled: ", player1_roll4)


player2_roll4 = random.randint(1, 6)
print("Player 2 rolled: ", player2_roll4)


input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll4 > player2_roll4:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll4," is greater than ", player2_roll4)
elif player1_roll4 == player2_roll4:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll4," is greater than ", player1_roll4)

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 winner, time for your chicken dinner! ")
elif player2_wins == 3:
    print("Player 2 winner, time for your chicken dinner! ")
else:
    print("this battle is at stalemate, pray to god that you win today!")

    input("\nPress ENTER to roll the dice...")
# round 5
player1_roll5 = random.randint(1, 6)
print("Player 1 rolled: ", player1_roll5)


player2_roll5 = random.randint(1, 6)
print("Player 2 rolled: ", player2_roll5)


input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll5 > player2_roll5:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll5," is greater than ", player2_roll5)
elif player1_roll5 == player2_roll5:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll5," is greater than ", player1_roll5)

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 winner, time for your chicken dinner! ")
elif player2_wins == 3:
    print("Player 2 winner, time for your chicken dinner! ")
else:
    print("this battle is at stalemate, pray to god that you win today!")

    input("\nPress ENTER to roll the dice...")
# round 6
player1_roll6 = random.randint(1, 6)
print("Player 1 rolled: ", player1_roll6)


player2_roll6 = random.randint(1, 6)
print("Player 2 rolled: ", player2_roll6)


input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll6 > player2_roll6:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll6," is greater than ", player2_roll6)
elif player1_roll6 == player2_roll6:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll6," is greater than ", player1_roll6)

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 winner, time for your chicken dinner! ")
elif player2_wins == 3:
    print("Player 2 winner, time for your chicken dinner! ")
else:
    print("this battle is at stalemate, pray to god that you win today!")

    input("\nPress ENTER to roll the dice...")
# round 7
player1_roll7 = random.randint(1, 6)
print("Player 1 rolled: ", player1_roll7)


player2_roll7 = random.randint(1, 6)
print("Player 2 rolled: ", player2_roll7)


input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll7 > player2_roll7:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll7," is greater than ", player2_roll7)
    print("here is the logbattle")
    print("Round: 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8")
    print("P1  : ", player1_roll, " | ", player1_roll2, " | ", player1_roll3, " | ", player1_roll4, " | ", player1_roll5, " | ", player1_roll6, " | ", player1_roll7, " | ")
    print("P2  : ", player2_roll, " | ", player2_roll2, " | ", player2_roll3, " | ", player2_roll4, " | ", player2_roll5, " | ", player2_roll6, " | ", player2_roll7, " | ")
elif player1_roll7 == player2_roll7:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll7," is greater than ", player1_roll7)
    print("here is the logbattle")
    print("Round: 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8")
    print("P1  : ", player1_roll, " | ", player1_roll2, " | ", player1_roll3, " | ", player1_roll4, " | ", player1_roll5, " | ", player1_roll6, " | ", player1_roll7, " | ")
    print("P2  : ", player2_roll, " | ", player2_roll2, " | ", player2_roll3, " | ", player2_roll4, " | ", player2_roll5, " | ", player2_roll6, " | ", player2_roll7, " | ")


# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 winner, time for your chicken dinner! ")
    print("here is the logbattle")
    print("Round: 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8")
    print("P1  : ", player1_roll, " | ", player1_roll2, " | ", player1_roll3, " | ", player1_roll4, " | ", player1_roll5, " | ", player1_roll6, " | ", player1_roll7, " | ")
    print("P2  : ", player2_roll, " | ", player2_roll2, " | ", player2_roll3, " | ", player2_roll4, " | ", player2_roll5, " | ", player2_roll6, " | ", player2_roll7, " | ")
elif player2_wins == 3:
    print("Player 2 winner, time for your chicken dinner! ")
    print("here is the logbattle")
    print("Round: 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8")
    print("P1  : ", player1_roll, " | ", player1_roll2, " | ", player1_roll3, " | ", player1_roll4, " | ", player1_roll5, " | ", player1_roll6, " | ", player1_roll7, " | ")
    print("P2  : ", player2_roll, " | ", player2_roll2, " | ", player2_roll3, " | ", player2_roll4, " | ", player2_roll5, " | ", player2_roll6, " | ", player2_roll7, " | ")
else:
    print("this battle is at stalemate, pray to god that you win today!")

    input("\nPress ENTER to roll the dice...")
# round 8
player1_roll8 = random.randint(1, 6)
print("Player 1 rolled: ", player1_roll8)


player2_roll8 = random.randint(1, 6)
print("Player 2 rolled: ", player2_roll8)


input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll8 > player2_roll8:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll8," is greater than ", player2_roll8)
    print("here is the logbattle")
    print("Round: 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8")
    print("P1  : ", player1_roll, " | ", player1_roll2, " | ", player1_roll3, " | ", player1_roll4, " | ", player1_roll5, " | ", player1_roll6, " | ", player1_roll7, " | ", player1_roll8)
    print("P2  : ", player2_roll, " | ", player2_roll2, " | ", player2_roll3, " | ", player2_roll4, " | ", player2_roll5, " | ", player2_roll6, " | ", player2_roll7, " | ", player2_roll8)
elif player1_roll8 == player2_roll8:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll8," is greater than ", player1_roll8)
    print("here is the logbattle")
    print("Round: 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8")
    print("P1  : ", player1_roll, " | ", player1_roll2, " | ", player1_roll3, " | ", player1_roll4, " | ", player1_roll5, " | ", player1_roll6, " | ", player1_roll7, " | ", player1_roll8)
    print("P2  : ", player2_roll, " | ", player2_roll2, " | ", player2_roll3, " | ", player2_roll4, " | ", player2_roll5, " | ", player2_roll6, " | ", player2_roll7, " | ", player2_roll8)

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 winner, time for your chicken dinner! ")
    print("here is the logbattle")
    print("Round: 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8")
    print("P1  : ", player1_roll, " | ", player1_roll2, " | ", player1_roll3, " | ", player1_roll4, " | ", player1_roll5, " | ", player1_roll6, " | ", player1_roll7, " | ", player1_roll8)
    print("P2  : ", player2_roll, " | ", player2_roll2, " | ", player2_roll3, " | ", player2_roll4, " | ", player2_roll5, " | ", player2_roll6, " | ", player2_roll7, " | ", player2_roll8)
elif player2_wins == 3:
    print("Player 2 winner, time for your chicken dinner! ")
    print("here is the logbattle")
    print("Round: 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8")
    print("P1  : ", player1_roll, " | ", player1_roll2, " | ", player1_roll3, " | ", player1_roll4, " | ", player1_roll5, " | ", player1_roll6, " | ", player1_roll7, " | ", player1_roll8)
    print("P2  : ", player2_roll, " | ", player2_roll2, " | ", player2_roll3, " | ", player2_roll4, " | ", player2_roll5, " | ", player2_roll6, " | ", player2_roll7, " | ", player2_roll8)
else:
    print("this battle is at stalemate, pray to god that you win today!")

    input("\nPress ENTER to roll the dice...")



# Since none of them would have won after 1 round, we could copy this code several times
# until we have enough times to make sure someone wins.


