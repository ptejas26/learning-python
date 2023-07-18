import random
# Variable 
# name = "Tejas"
# Funtion
def get_choices(): 
    options = ["rock", "paper", "scissors"]
    player_choice = input("Enter a choice " + ", ".join(options) + ": ")
    computer_choice = random.choice(options)
    choices = { "player": player_choice, "computer": computer_choice }
    return choices

def check_win(player, computer):
    # print("You chose " + player + ", computer chose " + computer)
    print(f"You chose {player}, computer chose {computer}")
    # if player == computer:
    #     return "It's a tie!"
    # elif player == "rock" and computer == "scissors":
    #     return "Rock smashes scissors! You Win!"
    # elif player == "rock" and computer == "paper":
    #     return "Paper covers rock! You lose."
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scrissors":
            return "Rock smashes scissors! You Win!"
        else: 
            return "Paper covers rock! You lose."
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You Win!"
        else: 
            return "Scissors cut paper! You lose."
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cut paper! You Win!"
        else: 
            return "Rock smashes scissors! You lose."


choices = get_choices()
result = check_win(choices["player"],choices["computer"])
print(result)

# food = ["pizza", "carrots", "eggs"]
# print(random.choice(food))

# Dictionary
#dict = { "name": "blueMan", "color": choices }
#print(dict)
