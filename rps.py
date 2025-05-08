responses = ["rock","paper","scissors"]
winlosetotal = []
loopcount = 1
bestof_input = input("Best of? 1 or 3 or 5").lower()

# this function is to do the initial check on bestof as to not run the entire game before the loop
def initialcheck(value):
    if value != "1" and value != "3" and value != "5":
        print("Please enter a valid option (1,3, or 5)")
    else:
        run()

# this function is to decide how many rounds are to be played.
def bestof_select(bestof):
    difficulty_input = input("Do you want the computer to respond randomly? (Type 'yes' or 'no')").lower()
    difficulty_select(difficulty_input)

# this function is to check if the player's guess is valid
def check(valid):
    if valid != "rock" and valid != "paper" and valid != "scissors":
        print("Please enter 'rock', 'paper', or 'scissors' only")

# this function is to decide the difficulty chosen by the user for the computer - random, always win, or always lose.
def difficulty_select(diff):
    global user_input
    if diff == "yes":
        user_input = input("Rock, Paper, or Scissors?").lower()
        check(user_input)
        comp_random_response()
    elif diff == "no":
        notrandomdiff_input = input("Do you want to always win, or always lose? (Type 'win' or 'lose')").lower()
        comp_win_lose(notrandomdiff_input)
    else:
        print("Please enter 'yes' or 'no'")

# this function will only run if difficulty_select has the output "no". This function is to decide if the computer
# will always win or lose.
def comp_win_lose(decision):
    if decision == "win":
        user_input = input("Rock, Paper, or Scissors?").lower()
        check(user_input)
        always_win(user_input) #player always wins
    elif decision == "lose":
        user_input = input("Rock, Paper, or Scissors?").lower()
        check(user_input)
        always_lose(user_input) #player always loses
    else:
        print("Please enter 'win' or 'lose'")

# this function is to check who won between the user and the random computer response
def winner_check(user,computer):
    if user == computer:
        print("It's a draw. Try Again!\n")
        winlosetotal.append("draw")
    elif user == "rock":
        if computer == "paper":
            print("YOU LOSE!!!!\n")
            winlosetotal.append("lose")
        else:
            print("Congratulations!! You WIN!!\n")
            winlosetotal.append("win")
    elif user == "scissors":
        if computer == "rock":
            print("YOU LOSE!!!!\n")
            winlosetotal.append("lose")
        else:
            print("Congratulations!! You WIN!!\n")
            winlosetotal.append("win")
    elif user == "paper":
        if computer == "scissors":
            print("YOU LOSE!!!!\n")
            winlosetotal.append("lose")
        else:
            print("Congratulations!! You WIN!!\n")
            winlosetotal.append("win")

# this function is for the random response that the computer is going to give
def comp_random_response():
    import random
    compguess = random.choice(responses)
    userguess = user_input
    print("Your guess: ",userguess)
    print("Computer guess: ",compguess)
    print()
    winner_check(userguess,compguess)

# this function is hardcode for the player always winning
def always_win(user_choice):
    if user_choice == "rock":
        print("scissors\nYou Win!\n")
        winlosetotal.append("win")
    elif user_choice == "paper":
        print("rock\nYou Win!\n")
        winlosetotal.append("win")
    else:
        print("paper\nYou Win!\n")
        winlosetotal.append("win")

# this function is hardcode for the player always losing
def always_lose(userchoice):
    if userchoice == "rock":
        print("paper\nYou Lose.\n")
        winlosetotal.append("lose")
    elif userchoice == "paper":
        print("scissors\nYou Lose.\n")
        winlosetotal.append("lose")
    else:
        print("rock\nYou Lose.\n")
        winlosetotal.append("lose")

# this function is to count the total number of rounds won, lost, or drawn
def final_standing():
    winnum = winlosetotal.count("win")
    losenum = winlosetotal.count("lose")
    drawnum = winlosetotal.count("draw")

    print("You won: ",winnum)
    print("You lost: ",losenum,)
    print("You drew: ",drawnum)

# this function is a loop to run the game for however many times stated in the bestof input
def run():
    global loopcount
    while loopcount <= int(bestof_input):
        print("\n",loopcount)
        bestof_select(bestof_input)
        loopcount += 1
    final_standing()

initialcheck(bestof_input)