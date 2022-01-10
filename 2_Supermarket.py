# import the random module
# use "winnings = random.randint(2, 10)" to generate a random int from 2 - 10 and store in a variable "winnings"
import random

# unit price of a lottery ticket
constant_lottery_unit_price = 2

# unit price of an apple
constant_apple_unit_price = .99

# unit price of a can of beans
constant_canned_beans_unit_price = 1.58

# unit price of a soda
constant_soda_unit_price = 1.23

# the user has initial $5 for shopping
money = 5

# the user has spent $0 initially
money_spent = 0

# the amounts of lottery tickets, apples, cans of beans, and sodas the user has purchased
lottery_amount, apple_amount, canned_beans_amount, soda_amount = 0, 0, 0, 0

# Print a welcome message along with a list of products and their unit prices
print("Welcome to the supermarket! Here's what we have in stock:")
print("- Lottery tickets cost ${} each".format(constant_lottery_unit_price))
print("- Apples cost ${} each".format(constant_apple_unit_price))
print("- Cans of beans cost ${} each".format(constant_canned_beans_unit_price))
print("- Sodas cost ${} each".format(constant_soda_unit_price))

# Purchase a lottery ticket or not?
print("\nYou have ${} available".format(money))
Lottery = input("First, do you want to buy a ${} lottery ticket for a chance at winning $2-$10? (y/n)".format(constant_lottery_unit_price))
if Lottery == 'y' or Lottery == 'Y':
    lottery_amount += 1
    # Random module of lottery ticket
    Probability = random.randint(0, 2)
    if Probability == 1:
        winnings = random.randint(2, 10)
        print("Congrats! You won ${}!".format(winnings))
    else:
        winnings = 0
        print("Sorry! You did not win the lottery.")
    money = money + winnings - constant_lottery_unit_price # Calculate money left
else:
    print("No lottery tickets were purchased.")
    winnings = 0

# Purchase apples or not?
print("\nYou have ${} available".format(money))
Apples = input("Do you want to buy apple(s)? (y/n)")
if Apples == 'y' or Apples == 'Y':
    Num = input("How many apple(s) do you want to buy?")
    try: # Test whether input is valid
        Num = int(Num)
        if Num > 0: # Test whether input is positive
            money_spent = Num * constant_apple_unit_price # Calculate cost
            print("The user wants to buy {} apple(s). This will cost ${}.".format(Num,money_spent))
            if money >= money_spent: # Estimate whether money is enough
                print("The user has enough money. {} apple(s) purchased.".format(Num))
                money = round(money - money_spent, 2) # Round the money to 2 digits
                apple_amount += Num # Record item number
            else:
                print("Not enough money! No apples purchased.")
        else:
            print("Positive values only! No apples selected.")
    except ValueError as e:
        print("Numerical values only! No apples selected.")
else:
    print("No apples were purchased.")

# Purchase beans or not?
print("\nYou have ${} available".format(money))
Beans = input("Do you want to buy can(s) of beans? (y/n)")
if Beans == 'y' or Beans == 'Y':
    Num = input("How many can(s) of beans do you want to buy?")
    try:
        Num = int(Num)
        if Num > 0:
            money_spent = Num * constant_canned_beans_unit_price
            print("The user wants to buy {} can(s) of beans. This will cost ${}.".format(Num,money_spent))
            if money >= money_spent:
                print("The user has enough money. {} can(s) of beans purchased.".format(Num))
                money = round(money - money_spent, 2)
                canned_beans_amount += Num
            else:
                print("Not enough money! No cans of beans purchased.")
        else:
            print("Positive values only! No cans of beans selected.")
    except ValueError as e:
        print("Numerical values only! No cans of beans selected.")
else:
    print("No cans of beans were purchased.")

# Purchase sodas or not?
print("\nYou have ${} available".format(money))
Sodas = input("Do you want to buy soda(s)? (y/n)")
if Sodas == 'y' or Sodas == 'Y':
    Num = input("How many soda(s) do you want to buy?")
    try:
        Num = int(Num)
        if Num > 0:
            money_spent = Num * constant_soda_unit_price
            print("The user wants to buy {} soda(s). This will cost ${}.".format(Num,money_spent))
            if money >= money_spent:
                print("The user has enough money. {} soda(s) purchased.".format(Num))
                money = round(money - money_spent, 2)
                soda_amount += Num
            else:
                print("Not enough money! No sodas purchased.")
        else:
            print("Positive values only! No sodas selected.")
    except ValueError as e:
        print("Numerical values only! No sodas selected.")
else:
    print("No sodas were purchased.")
    
# List of products and money left
print("\nMoney left: ${}".format(money))
print("Lottery ticket(s) purchased: {}".format(lottery_amount))
print("Lottery winnings: {}".format(winnings))
print("Apple(s) purchased: {}".format(apple_amount))
print("Can(s) of beans purchased: {}".format(canned_beans_amount))
print("Soda(s) purchased: {}".format(soda_amount))
print("Good bye!")

