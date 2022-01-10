# import the random module
# use "random_int = randint(1, 13)" to generate a random int from 1 - 13 and store in a variable "random_int"
from random import randint


def print_instructions():
    """
    This function prints out instructions for the game.
    """
    print("Let's play Simple21!\nYou'll play against the computer.\nTry to get as close to 21 as possible, without going over.")
    


def ask_yes_or_no(prompt):
    """
    This function displays the given prompt and asks the user for input. If the user's input starts with 'y', returns True.
    If the user's input starts with 'n', returns False.
    Else, the input is invalid, prompt the question again until the user gives a valid input.
    For example, calling ask_yes_or_no("Do you want to play again? (y/n)")
    would display "Do you want to play again? (y/n)", wait for user input that starts with 'y' or 'n',
    and return True or False accordingly.
    """
    answer = input(prompt)
    #strips whitespace from beginning and end of entire string
    answer = answer.strip()
    
    #If the user’s input is invalid, prompt the question again until a valid input.
    while answer[0] != 'Y' and answer[0] != 'y' and answer[0] != 'N' and answer[0] != 'n':
        answer = input(prompt) 
        answer = answer.strip()
    if answer[0] == 'Y' or answer[0] == 'y':
        return True
    elif answer[0] == 'N' or answer[0] == 'n':
        return False

        
def next_card():
    """
    This function returns a random "card", represented by an int between 1 and 10, inclusive.
    The "cards" are the numbers 1 through 10 and they are randomly generated, not drawn from a deck of
    limited size. The odds of returning a 10 are four times as likely as any other value (because in an
    actual deck of cards, 10, Jack, Queen, and King all count as 10).
    """
    # Generate random int between 1~13
    random_int = randint(1, 13)
    # Make the odds of returning a 10 are four times as likely as any other value
    if random_int < 10:
        card = random_int
    else:
        card = 10
    return card


def take_another_card(computer_total_points, user_visible_card):
    """
    This function is the strategy for computer to take another card or not. According to the computer’s own given
    total points (sum of visible cards + hidden card) and the user's sum of visible cards.
    The strategy is: the computer decides to stop taking another card when its total points is over 15 and
    user_visible_card is smaller than computer's total card, otherwise, the computer decides to take another card.
    Returns True if the strategy decides to take another card, False if the computer decides not
    to take another card.
    """
    # Strategy: stop taking another card when computer total points > 15 and more than user visible card
    if computer_total_points <= 21:
        if computer_total_points > 15 and user_visible_card < computer_total_points:
            return False
        else:
            return True
    else:
        return False


def is_game_over(is_user_passed, is_computer_passed):
    """
    This function determines if the game is over or not.
    If the given is_user_passed is set to True, the user has passed.
    If the given is_computer_passed is set to True, the computer has passed.
    This function returns True if both the user and the computer have passed,
    and False if either of them has not yet passed.
    """
    if is_user_passed == True and is_computer_passed == True:
        return True
    else:
        return False

def print_status(is_user, name, hidden_card, visible_card, total_points):
    """
    In each turn, prints out the current status of the game.
    If is_user is set to True, the given player is the user. In this case, print out
    the user's given name, his/her hidden card points, visible card points, and total points.
    If is_user is set to False, the given player is the computer.  In this case, print out
    the computer's given name, and his/her visible card points.

    For example, calling print_status(True, "Brandon", 4, 15, 19) would print:
    Brandon has 4 hidden point(s).
    Brandon has 15 visible point(s).
    Brandon has 19 total point(s).

    As another example, calling print_status(False, "Computer", 1, 19, 20) would print:
    Computer has 19 visible point(s).
    """
    if is_user == True:
        print("{} has {} hidden point(s)".format(name, hidden_card))
        print("{} has {} visible point(s)".format(name, visible_card))
        print("{} has {} total point(s)".format(name, total_points))
    else:
        print("{} has {} visible point(s)".format(name, visible_card))


def print_winner(username, user_total_points, computer_name, computer_total_points):
    """
    This function determines who won the game and prints the game results in the following format:
    - User's given name and the given user's total points
    - Computer's given name and the given computer's total points
    - The player who won the game and the total number of points he/she won by, or if it's a tie, nobody won.
    - It is a tie when computer and user have the same card points and both of them are not over 21.
    If both of them go over 21, then nobody wins.
    - The winning points is calculated by substracting the loser's points from the winner's points.
    """
    print("-- Game Over --")
    print("{} has {} in total.".format(username, user_total_points))
    print("{} has {} in total.".format(computer_name, computer_total_points))
    if user_total_points <= 21 and computer_total_points <= 21:
    # while both <= 21, win if total points closer to 21, tie if equal
        if user_total_points > computer_total_points:
            print("{} wins by {} point(s)".format(username, user_total_points - computer_total_points))
        elif user_total_points < computer_total_points:
            print("{} wins by {} point(s)".format(computer_name, computer_total_points - user_total_points))
        else:
            print("Nobody wins. It's a tie!")
    # while one is over 21, the other one wins
    elif user_total_points > 21 and computer_total_points <= 21:
        print("{} wins by {} point(s)".format(computer_name, user_total_points - computer_total_points))

    elif user_total_points <= 21 and computer_total_points > 21:
        print("{} wins by {} point(s)".format(username, computer_total_points - user_total_points))
    # while both are over 21, nobody wins
    else:
        print("Nobody wins. Everyone goes over 21!")


def run(username, computer_name):
    """
    This function controls the overall game and logic for the given user and computer.
    First, this function gives initial hidden cards and visible cards to both players and print it.
    Then, both players can take a card until they pass, individually.
    When both players pass the game, print the game result.
    """
    # randomly get initial hidden cards and visible cards
    user_hidden_card = next_card()
    user_visible_card = next_card()
    user_total_points = user_hidden_card + user_visible_card
    print_status(True, username, user_hidden_card, user_visible_card, user_total_points)
    computer_hidden_card = next_card()
    computer_visible_card = next_card()
    computer_total_points = computer_hidden_card + computer_visible_card
    print_status(False, computer_name, computer_hidden_card, computer_visible_card, computer_total_points)
    is_user_passed = False
    is_computer_passed = False

    # For user, get a random visible card if answering 'y' or 'Y'. Pass when answering 'n' or 'N'.
    while is_game_over(is_user_passed, is_computer_passed) == False:
        if is_user_passed == False:
            answer = ask_yes_or_no('Take another card? (y/n) ')
            if answer == True:
                is_user_passed = False
                new_card = next_card()
                user_visible_card += new_card
                user_total_points = user_hidden_card + user_visible_card
                print("{} gets {}".format(username, new_card))
                print_status(True, username, user_hidden_card, user_visible_card, user_total_points)
            else:
                is_user_passed = True
                print("{} passed!".format(username))
            
    # For computer, get a random visible card according to its own strategy. 
        if is_computer_passed == False:
            if take_another_card(computer_total_points, user_visible_card) == True:
                is_computer_passed = False
                new_card = next_card()
                computer_visible_card += new_card
                computer_total_points = computer_hidden_card + computer_visible_card
                print("{} gets {}".format(computer_name, new_card))
                print_status(False, computer_name, computer_hidden_card, computer_visible_card, computer_total_points)            
            else:
                is_computer_passed = True
                print("{} passed!".format(computer_name))
    # When both user and computer pass, print the result
    print_winner(username, user_total_points, computer_name, computer_total_points)
    return


def main():
    """
    Main Function.
    """

    # print the game instructions
    print_instructions()

    # get and set user's name
    username = input("What's your name?\r\n")

    # set computer's name
    computer_name = "Computer"

    # run the game
    run(username, computer_name)

    # ask the user whether to play again, stop the game if not.
    while 1 == 1:
        play_again = ask_yes_or_no("Play again? (y/n) ")
        if play_again == True:
            # ask the user whether to modify the name or not
            Modify_name = ask_yes_or_no("Modify username? (y/n) ")
            if Modify_name == True:
                username = input("Update your name?\r\n")
            else:
                username = username
            run(username, computer_name)
        else:
            break


if __name__ == '__main__':
    main()
