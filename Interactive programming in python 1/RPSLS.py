import random

def name_to_number(name):
    """
    Returns a unique number for each name, given the name as input.
    """
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print("Incorrect input. Try again ")



def number_to_name(number):
    """
    Returns the name coresponding the number, given the number as input
    """
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        pass


def rpsls(player_choice):
    """
    Given a name, this function prints out who wins the game (you or the computer) based on the the game rules
    """
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5)
    print("Player chooses {}".format(number_to_name(player_number)))
    print("Computer chooses {}".format(number_to_name(comp_number)))
    diff = (player_number - comp_number) % 5
    if diff == +1 or diff == +2:
        print("Player wins \n")
    elif diff == +3 or diff == +4:
        print("Computer wins \n")
    elif diff == 0:
        print("Player Computer tie ! \n")
    else:
        print("Try again")



# Here , it keeps asking for the input, until a valid input is typed in.
# The valid inputs are "rock", "Spock", "paper", "lizard", "scissors" - case sensitive
while True:
    x = input("Enter your choice(rock/Spock/paper/lizard/scissors): ")
    if x not in ["rock", "paper", "lizard", "scissors", "Spock"]:
        print("Please check the input and try again")
        continue
    else:
        break
rpsls(x)
