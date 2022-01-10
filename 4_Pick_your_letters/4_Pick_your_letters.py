import random
import string


def read_from_file(file_name):
    """
    Reads all words from file
    Parameter file_name is the name of the file
    This function returns a list containing all the words
    """
    f = open(file_name, "r")
    all_words = f.read().splitlines()
    f.close()
    return all_words


def ask_for_length():
    """
    Ask the user for the number of hand cards,
    and prompt again if invalid input.
    """
    # ask for length
    L = input("Enter a number between 3 - 10 to be length of the word you are going to guess:\r\n")

    # If the input is out of range or not integer, prompt again.
    while True:
        if L.isdigit():
            L = int(L)
            if 3 <= L <= 10:
                return L
            else:
                L = input("Enter a number between 3 - 10 to be length of the word you are going to guess:\r\n")
        else:
            L = input("Enter a number between 3 - 10 to be length of the word you are going to guess:\r\n")


def filter_word_list(all_words, length):
    """
    This function returns a specific list of words with the length the user chooses.
    The words are withdraw from the all_words list.
    """
    # TODO
    # Construct a list to store the length of word.
    num = []

    # Construct a list to store the filtered words.
    word_list = []

    # Construct a list to store the word and its length.
    word_list_with_num = []

    # Put word and its length into a tuple. Store in a list.
    for i in all_words:
        num.append(len(i))
        word_list_with_num.append((i, num[-1]))

    # Sort the list by the length of word.
    word_list_with_num = sorted(word_list_with_num)

    # Choose the words whose length are equal to the specific length that the user chose, store in word_list
    for i in word_list_with_num:
        if i[1] == length:
            word_list.append(i[0])
    return word_list


def set_up(length):
    """
    This function creates a main pile of 26 * length cards,
    represented as a list of lowercase letters, with length of each letter.
    Then, it creates a discard pile of 0 card, and return both lists as a tuple
    """
    # TODO
    # Put all lowercase characters in a list
    letter = string.ascii_lowercase
    letter_lst = []
    for i in letter:
        letter_lst.append(i)

    # Create main_pile with every character have * length cards
    main_pile = letter_lst * length

    # Create a discard pile
    discard_pile = []
    return main_pile, discard_pile


def shuffle_cards(pile):
    """
    This function shuffles the given pile
    """
    # TODO
    random.shuffle(pile)
    return pile


def move_to_discard_pile(discard_pile, card):
    """
    This function moves the given card to the top of the discard_pile.
    """
    # TODO
    discard_pile.insert(0, card)


def deal_initial_cards(main_pile, discard_pile, length):
    """
    This function deals two sets of length cards to the computer and the user as initial.
    It removes the card on top of the main pile and put it on the discard pile.
    This function returns the initial cards of the computer and the user as a tuple.
    """
    # TODO
    computer_pile = []
    user_pile = []
    for i in range(0, length):
        computer_pile.append(main_pile[0])  # Computer takes a card from the top of main pile
        main_pile.pop(0)
        user_pile.append(main_pile[0])  # User takes a card from the top of main pile
        main_pile.pop(0)
    discard_pile.append(main_pile[0])  # Move the card on the top of the main pile to the discard pile
    main_pile.pop(0)
    return computer_pile, user_pile


def get_first_from_pile_and_remove(pile):
    """
    This function returns and removes the first item of the given list
    """
    # TODO
    top_element = pile[0]
    pile.pop(0)
    return top_element


def computer_play(computer_hand_cards, computer_target_list, main_pile, discard_pile):
    """
    This is the game strategy of the computer.
    First, the computer tests whether the top card in the discard pile is same to
    some card needed to be replaced in the target list.
    If so, the computer takes the top card in the discard pile and discards its own card;
    if not, the computer decides to see the top card of the main pile.
    Then, the computer tests whether the top card in the main pile is same to
    some card needed to be replaced in the target list.
    If so, the computer takes the top card in the main pile and discard its own card;
    if not, the computer discards the card to the discard pile.

    """
    # TODO
    print("Computer's turn")
    # Construct a flag to record whether the computer takes the card from the discard pile. 
    flag_discard = False

    # Find whether there is a card can be replaced by the card from discard pile that can helps make a word.
    for i in computer_target_list:
        for j in range(0, len(computer_hand_cards)):
            if computer_hand_cards[j] != i[j] and discard_pile[0] == i[j]:
                computer_hand_cards[j] = discard_pile[0]
                print("Computer took \'" + discard_pile[0] + "\' from DISCARD PILE")
                discard_pile.pop(0)
                flag_discard = True
                break

    # Construct a flag to record whether the computer takes the card from the main pile.
    flag_main = False

    # Find whether there is a card can be replaced by the card from main pile that can helps make a word.
    if not flag_discard:
        for i in computer_target_list:
            for j in range(0, len(computer_hand_cards)):
                if computer_hand_cards[j] != i[j] and main_pile[0] == i[j]:
                    computer_hand_cards[j] = main_pile[0]
                    print("Computer took \'" + main_pile[0] + "\' from MAIN PILE")
                    main_pile.pop(0)
                    flag_main = True
                    break

    # If no card can be replaced, discard the top card from the main pile to the discard pile.
    if not flag_main:
        discard_pile.insert(0, main_pile[0])
        main_pile.pop(0)
        print("Computer discarded \'" + main_pile[0] + "\' from MAIN PILE")


def ask_for_the_letter_to_be_replaced(length):
    """
    This function asks for the index of letter that the user wants to be replaced.
    Parameter length is the length is the number of cards in the user's hand.

    """
    # TODO
    replaced_index = input('Input the index of the letter to be replaced, e.g. \'1\':\r\n')
    # Prompt again if invalid
    while True:
        try:
            replaced_index = int(replaced_index)
            if 0 <= replaced_index < length:
                break
            while replaced_index < 0 or replaced_index >= length:
                print('Index out of range')
                replaced_index = input('Input the index of the letter to be replaced, e.g. \'1\':\r\n')
                replaced_index = int(replaced_index)
        except:
            print('Please enter a valid integer')
            replaced_index = input('Input the index of the letter to be replaced, e.g. \'1\':\r\n')

    return replaced_index


def ask_yes_or_no(msg):
    """
    This function displays msg and return user's answer
    """
    # TODO
    answer = input(msg + '\r\n')

    # Strip the empty spaces in the input
    answer = answer.strip()

    # Transfer the input into lowercase
    answer = answer.lower()

    # Prompt again if invalid input
    while answer != 'y' and answer != 'n' and answer != 'yes' and answer[0] != 'no':
        answer = input(msg + '\r\n')
        answer = answer.strip()
        answer = answer.lower()

    if answer == 'y' or answer == 'yes':
        return True
    elif answer == 'n' or answer == 'no':
        return False


def check_game_over(human_hand_cards, computer_hand_cards, words_with_specific_length):
    """
    This function checks whether the game is over.

    """
    # TODO

    # Construct a flag to record the status of the game
    game = False

    # Construct a flag to record the status of the user
    human = False

    # Construct a flag to record the status of the computer
    computer = False
    # Transfer the user's and computer's cards from list to string
    separator = ''
    human_hand_word = separator.join(human_hand_cards)
    computer_hand_word = separator.join(computer_hand_cards)

    # Test whether the user makes a word
    for i in words_with_specific_length:
        if human_hand_word == i:
            human = True
            break

    # Test whether the computer makes a word
    for i in words_with_specific_length:
        if computer_hand_word == i:
            computer = True
            break

    # Output the result if one of them succeeds.
    if human:
        if computer:
            print("Tie!")
            print("Computer's word is " + computer_hand_word)
            print("Your word is " + human_hand_word)
            game = True
        else:
            print("You win!")
            print("Your word is " + human_hand_word)
            game = True
    else:
        if computer:
            print("Computer wins!")
            print("Computer's word is " + computer_hand_word)
            game = True

    return game


def check_bricks(main_pile, discard_pile):
    """
    Check whether the main_pile is empty.
    If so, shuffle the discard_pile and move all the cards to the main_pile,
    take the first card from main_pile to the discard_pile.
    If not, do nothing.
    """
    if len(main_pile) == 0:  # Check whether the main_pile if empty.
        random.shuffle(discard_pile)  # Shuffle the discard_pile
        main_pile[:] = discard_pile[:]  # Move all the cards from the discard_pile to the main_pile
        discard_pile[:] = []  # Clear the discard_pile
        card = get_first_from_pile_and_remove(main_pile)  # Take the first card from main_pile to the discard_pile
        move_to_discard_pile(discard_pile, card)


def filter_computer_target_list_helper(computer_hand_cards, word_list):
    """
    This function scores the similarity between computer_hand_cards and words in word_list.
    And choose the words with highest similarity to be computer_target_list
    """
    score = []
    words_with_score = []

    # Record the number of cards with correct position and value as score.
    for i in word_list:
        a = 0
        for j in range(0, len(computer_hand_cards)):
            if computer_hand_cards[j] == i[j]:
                a += 1
            score.append(a)
        words_with_score.append((i, score[-1]))  # Put the word the its score in a tuple, and store in a list

    # Sort the list by score.
    words_with_score = sorted(words_with_score)

    # Take the words with highest score from the word_list as computer's target list
    highest_score = words_with_score[0][0]
    computer_target_list = []
    for i in words_with_score:
        if i[1] == highest_score:
            computer_target_list.append(i[0])
    return computer_target_list


def pick_from_discard_or_main_pile_helper(discard_pile):
    """
    This function asks user if he/she wants to choose from discard_pile or main_pile.
    If he/she wants to choose from the discard_pile, return False.
    If he/she wants to choose from the main_pile, return True.
    """
    card = discard_pile[0]
    answer = input('Pick \'' + card + '\' from DISCARD PILE or reveal the letter from MAIN PILE \n'
                   + "Reply 'D' or 'M' to respond:\n")
    answer = answer.strip()
    answer = answer.lower()
    while answer != 'm' and answer != 'd':
        print('Please enter a valid response')
        answer = input('Pick \'' + card + '\' from DISCARD PILE or reveal the letter from MAIN PILE \n'
                       + "Reply 'D' or 'M' to respond:\n")
        answer = answer.strip()
        answer = answer.lower()
    if answer == 'm':
        return True
    elif answer == 'd':
        return False


def main():
    # reads all words from file
    all_words = read_from_file("words.txt")

    print("Welcome to the game!")

    # ask for a number as the length of the word
    length = ask_for_length()

    # filter all_words with a length equal to the given length
    word_list = filter_word_list(all_words, length)

    # set up main_pile and discard_pile
    pile = set_up(length)
    main_pile = pile[0]
    discard_pile = pile[1]

    # shuffle main pile
    shuffle_cards(main_pile)

    # deal cards to players, creating human_hand_cards and computer_hand_cards
    # and initialize discard pile
    initial = deal_initial_cards(main_pile, discard_pile, length)
    computer_pile = initial[0]
    user_pile = initial[1]

    # start the game
    while True:
        # computer play goes here

        # Check bricks
        check_bricks(main_pile, discard_pile)

        # Filter target list
        computer_target_list = filter_computer_target_list_helper(computer_pile, word_list)

        # Computer play
        computer_play(computer_pile, computer_target_list, main_pile, discard_pile)

        # Print the status
        print("Computer's current hand is:")
        print(computer_pile)
        print("-----------------------------------------------")

        # human play goes here
        # Check bricks
        check_bricks(main_pile, discard_pile)

        print("Your turn")

        # Print the status
        print("Your word list is:")
        print(user_pile)

        # Ask the user to choose from the discard pile or the main pile
        choice = pick_from_discard_or_main_pile_helper(discard_pile)

        # Choose from main_pile
        if choice:
            chosen_element = get_first_from_pile_and_remove(main_pile)
            print("The letter from MAIN PILE is \'" + chosen_element + "\'")

            # Ask the user whether to accept it or not
            ans = ask_yes_or_no("Do you want to accept this letter? Type 'y/yes' to accept, 'n/no' to discard.")
            if ans:  # accept the card from main_pile
                replaced_index = ask_for_the_letter_to_be_replaced(length)
                move_to_discard_pile(discard_pile, user_pile[replaced_index])
                print("You replaced \'" + user_pile[replaced_index] + "\' with \'" + chosen_element + "\'")
                user_pile[replaced_index] = chosen_element
            else:  # not accept the card from main_pile
                move_to_discard_pile(discard_pile, chosen_element)
                print("You discarded \'" + chosen_element + "\' from MAIN PILE")

        # Choose from discard_pile
        else:
            chosen_element = get_first_from_pile_and_remove(discard_pile)
            replaced_index = ask_for_the_letter_to_be_replaced(length)
            move_to_discard_pile(discard_pile, user_pile[replaced_index])
            print("You replaced \'" + user_pile[replaced_index] + "\' with \'" + chosen_element + "\'")
            user_pile[replaced_index] = chosen_element

        # Print the status
        print("Your word list is:")
        print(user_pile)
        print("-----------------------------------------------")

        # check if game is over and print out results

        check = check_game_over(user_pile, computer_pile, word_list)
        if check:
            break


if __name__ == "__main__":
    main()
