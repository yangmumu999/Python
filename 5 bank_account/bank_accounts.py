def init_bank_accounts(accounts, deposits, withdrawals):
    """
    This function loads the given 3 files,
    stores the information for individual bank accounts in a dictionary
    and calculates the account balance.
    The returned band_accounts dictionary includes the account number, name, and balance.
    """
    bank_accounts = {}

    # open accounts file
    f1 = open(accounts, "r")

    # store every line in the file in a list as string
    account_lines = f1.readlines()

    # convert string into list, and store the information in a dictionary
    for line in account_lines:
        lst = line.strip().split("|")
        account_number = lst[0].strip()
        first_name = lst[1].strip()
        last_name = lst[2].strip()
        bank_accounts.update({account_number: {'first_name': first_name, 'last_name': last_name, 'balance': 0}})
    f1.close()

    # extract deposit information from the file, and store in a list as strings.
    f2 = open(deposits, "r")
    deposits_lines = f2.readlines()

    # convert string to list, and deposit the money in corresponding account
    for line in deposits_lines:
        lst = line.split(",")
        account_number = str(lst[0].strip())
        deposit_sum = 0
        for i in lst[1:]:
            deposit_sum += float(i.strip())
        deposit(bank_accounts, account_number, deposit_sum)
    f2.close()

    # read withdraw information and store in a list as strings
    f3 = open(withdrawals, "r")
    withdraw_lines = f3.readlines()

    # convert string to list, and withdraw money from corresponding account
    for line in withdraw_lines:
        lst = line.split(",")
        num = str(lst[0].strip())
        withdraw_sum = 0
        for i in lst[1:]:
            withdraw_sum += float(i.strip())
        withdraw(bank_accounts, num, withdraw_sum)
    f3.close()

    return bank_accounts


def get_account_info(bank_accounts, account_number):
    """
    This function returns the account information for the given account_number as a dictionary.
    If the account_number does not exist, return None.
    """
    try:
        account_number = int(account_number)
        if 0 < int(account_number) <= len(bank_accounts):
            info = bank_accounts[str(account_number)]
        else:
            return None
    except ValueError as e:
        return None
    return info


def withdraw(bank_accounts, account_number, amount):
    """
    This function withdraws the given amount of money from the given account.
    The new balance is rounded to 2 decimal places and is printed out.
    """
    if 0 < int(account_number) <= len(bank_accounts):
        # get the deposit of the account
        account_deposit = bank_accounts.get(account_number)['balance']

        # return RuntimeError if there is not enough money to withdraw
        if amount > account_deposit:
            raise RuntimeError('Not enough money!')

        # calculate new balance after withdraw and round it, renew the bank_accounts dictionary
        else:
            new_balance = account_deposit - amount
            bank_accounts.get(account_number)['balance'] = new_balance
            round_balance(bank_accounts, account_number)
        print('New balance: ' + str(bank_accounts.get(account_number)['balance']))
    else:
        print('Sorry, that account does not exist.')


def deposit(bank_accounts, account_number, amount):
    """
    This function deposits the given amount of money into the given account.
    The new balance is rounded to 2 decimal places and is printed out.
    """
    if 0 < int(account_number) <= len(bank_accounts):
        # get the balance information of the account
        balance = bank_accounts.get(account_number)['balance']

        # calculate new balance from old balance and deposit amount
        new_balance = balance + amount

        # round the new balance and renew it in the dictionary
        bank_accounts.get(account_number)['balance'] = new_balance
        round_balance(bank_accounts, account_number)
        print('New balance: ' + str(bank_accounts.get(account_number)['balance']))
    else:
        print('Sorry, that account does not exist.')


def calculate_sales_tax(amount):
    """
    This function calculates the tax of total amounts from the input amount list.
    """
    tax = 0.06 * amount
    return tax


def purchase(bank_accounts, account_number, amounts):
    """
    This function makes a purchase with the total of the given amounts from the account with the given account_number.
    The total purchase is the sum of total amounts and 6% tax.
    This function prints the new balance after calculating.
    """
    # check whether the account_number is integer.
    try:
        account_number = int(account_number)
    except:
        print('Sorry, that account does not exist.')
        return None
    # calculate total amounts from the list of amounts, and add tax.
    account_number = str(account_number)
    if 0 < int(account_number) <= len(bank_accounts):
        balance = bank_accounts.get(account_number)['balance']
        total_amounts = 0
        for i in amounts:
            i = str(i).strip()
            total_amounts += float(i)
        tax = calculate_sales_tax(total_amounts)
        total_purchase = total_amounts + tax
        # raise error when balance is not enough to purchase.
        if total_purchase > balance:
            raise RuntimeError('Not enough money!')
        else:
            # minus the total purchase from the balance, renew the balance
            withdraw(bank_accounts, account_number, total_purchase)
    else:
        print('Sorry, that account does not exist.')


def export_statement(bank_accounts, account_number, output_file):
    """
    This function exports the given account information to the given output file,
    with first name, last name, and balance.
    """
    # obtain account information and write them in a .txt file
    if int(account_number) <= len(bank_accounts) + 1:
        info = get_account_info(bank_accounts, account_number)
        f = open(output_file, 'w')
        for key in info:
            f.writelines(str(key) + ': ' + str(info.get(key)) + '\n')
        f.close()
    else:
        print('Sorry, that account does not exist.')


def sort_accounts(bank_accounts, sort_type, sort_direction):
    """
    This function converts the key:value pairs in the given bank_accounts dictionary
    to a list of tuples and sorts based on the given sort_type and sort_direction,
    and returns the sorted list of tuples.
    """
    # convert the bank_accounts dictionary into a list of tuples.
    bank_accounts_lst = []
    for key in bank_accounts:
        bank_accounts_lst.append((key, bank_accounts[key]))

    # sort the list according to the sort_type and sort_direction
    if sort_type == 'account_number':
        if sort_direction == 'asc':
            bank_accounts_lst = sorted(bank_accounts_lst, key=lambda item: int(item[0]))
        else:
            bank_accounts_lst = sorted(bank_accounts_lst, key=lambda item: int(item[0]), reverse=True)
    elif sort_type == 'first_name' or sort_type == 'last_name':
        if sort_direction == 'asc':
            bank_accounts_lst = sorted(bank_accounts_lst, key=lambda item: str(item[1][sort_type]))
        else:
            bank_accounts_lst = sorted(bank_accounts_lst, key=lambda item: str(item[1][sort_type]), reverse=True)
    elif sort_type == 'balance':
        if sort_direction == 'asc':
            bank_accounts_lst = sorted(bank_accounts_lst, key=lambda item: float(item[1][sort_type]))
        else:
            bank_accounts_lst = sorted(bank_accounts_lst, key=lambda item: float(item[1][sort_type]), reverse=True)
    else:
        print("The sort_type is not acceptable.")
        return None
    return bank_accounts_lst


def round_balance(bank_accounts, account_number):
    """
    This function rounds the account balance of the given account_number to two decimal places
    """
    # get current balance
    balance = bank_accounts.get(account_number)['balance']
    # round the balance to 2 decimal
    balance = round(balance, 2)
    # renew the balance
    bank_accounts.get(account_number)['balance'] = balance


def choose_action_helper():
    """
    This function asks the user to choose the service he/she wants.
    Invalid input will be required to input again.
    Input '0' if the user wants to stop the service.
    """
    action = input("1: Get account info\n" +
                   "2: Make a deposit\n" +
                   "3: Make a withdrawal\n" +
                   "4: Make a purchase\n" +
                   "5: Sort accounts\n" +
                   "6: Export a statement\n" +
                   "0: Leave the bank\n")
    # check whether the input is integer and valid
    while True:
        try:
            action = int(action)
            if 0 <= action <= 6:
                break
            else:
                print("Your input is out of range. Please input again.")
                action = input("1: Get account info\n" +
                               "2: Make a deposit\n" +
                               "3: Make a withdrawal\n" +
                               "4: Make a purchase\n" +
                               "5: Sort accounts\n" +
                               "6: Export a statement\n" +
                               "0: Leave the bank\n")
        except ValueError as e:
            print("Your input is invalid. Please input an integer.")
            action = input("1: Get account info\n" +
                           "2: Make a deposit\n" +
                           "3: Make a withdrawal\n" +
                           "4: Make a purchase\n" +
                           "5: Sort accounts\n" +
                           "6: Export a statement\n" +
                           "0: Leave the bank\n")
    return action


def main():
    # store bank information in a dictionary
    bank_accounts = init_bank_accounts('accounts.txt', 'deposits.csv', 'withdrawals.csv')

    print("Welcome to the bank! What would you like to do?")
    # Start the service
    while True:
        action = choose_action_helper()
        if action == 0:
            print("Good bye!")
            break
        if action == 1:
            # get account number
            account_number = input("Account number?\n")
            # print the account information
            account_info = get_account_info(bank_accounts, account_number)
            print(account_info)
            print('\n')
        if action == 2:
            account_number = input("Account number?\n")
            deposit_amount = input('How much do you want to deposit?\n')
            # check whether the input is valid
            try:
                deposit_amount = float(deposit_amount)
                # deposit the amount of money into account
                deposit(bank_accounts, account_number, deposit_amount)
            except ValueError as e:
                print("Your input is invalid.")
            print('\n')
        if action == 3:
            account_number = input("Account number?\n")
            withdraw_amount = input('How much do you want to withdraw?\n')
            # check whether the input is valid
            try:
                withdraw_amount = float(withdraw_amount)
                # withdraw the amount of money from the acount
                withdraw(bank_accounts, account_number, withdraw_amount)
            except ValueError as e:
                print("Your input is invalid.")
                print('\n')
        if action == 4:
            account_number = input("Account number?\n")
            purchase_amount = input('Purchase amounts? (Please input as comma separated list)\n')
            # convert the input from string to list
            amounts = purchase_amount.split(',')
            # check whether the input is valid
            valid_or_not = False
            for i in amounts:
                try:
                    i = float(i)
                    valid_or_not = True
                except ValueError as e:
                    print("Your input is non-numeric.")
                    valid_or_not = False
                    break
            # for valid input, subtract the purchase amount from the balance
            if valid_or_not:
                purchase(bank_accounts, account_number, amounts)
        if action == 5:
            # ask sort_type
            sort_type = input('Sort type? (account_number, first_name, last_name, balance)\n')
            # ask sort_direction
            sort_direction = input("Sort direction? ('asc' for ascending, 'desc' for descending)\n")
            # sort bank_accounts according to the instruction and print out
            sorted_accounts = sort_accounts(bank_accounts, sort_type, sort_direction)
            print(sorted_accounts)
        if action == 6:
            account_number = input("Account number?\n")
            # create a .txt file named by account number
            export_statement(bank_accounts, account_number, account_number + '.txt')


if __name__ == "__main__":
    main()
