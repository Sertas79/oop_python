# Без ООП
# Банк. Версия 5
# Любое количество счетов - со списком словарей

accountsList = []

def newAccount(aName, aBalance, aPassword):
    global accountsList
    newAccountDict = {'name':aName, 'balance':aBalance, 'password':aPassword}
    accountsList.append(newAccountDict)

def show(accountNumber):
    global accountsList
    print('Account', accountNumber)
    thisAccountDict = accountsList[accountNumber]
    print('     Name', thisAccountDict['name'])
    print('     Balance', thisAccountDict['balance'])
    print('     Password:', thisAccountDict['password'])
    print()

def getBalance(accountNumber, password):
    global accountsList
    thisAccountDict = accountsList[accountNumber]
    if password != thisAccountDict['password']:
        print('Incorrect password')
        return None
    return thisAccountDict['balance']

def deposit(accountNumber, amountToDeposit, password):
    global accountsList
    thisAccountDict = accountsList[accountNumber]
    if amountToDeposit < 0:
        print('You connot deposit a negative amount!')
        return None
    
    if password != thisAccountDict['password']:
        print('Incorrect password')
        return None

    thisAccountDict['balance'] = thisAccountDict['balance'] + amountToDeposit
    return thisAccountDict['balance']

def withdraw(accountNumber, amountToWithdraw, password):
    global accountsList
    thisAccountDict = accountsList[accountNumber]
    if amountToWithdraw < 0:
        print('You cannot withdraw a negative amount')
        return None
    
    if password != thisAccountDict['password']:
        print('Incorrect password')
        return None
    
    if amountToWithdraw > thisAccountDict['balance']:
        print('You cannot withdraw more than you have in your account')
        return None
    
    thisAccountDict['balance'] = thisAccountDict['balance'] - amountToWithdraw
    return thisAccountDict['balance']

print('Joe`s account is account number:', len(accountsList))
newAccount('Joe', 100, 'soup')

print('Mary`s account is account number:', len(accountsList))
newAccount('Mary', 12345, 'nuts')

while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press n to create a new account')
    print('Press w to make a withdrawal')
    print('Press s to show the account')
    print('Press q to quit')
    print()

    action = input('What do you want to do? ')
    action = action.lower() # переоводим в нижний регистр
    action = action[0] # используем первую букву
    print()

    if action == 'b':
        print('Get Balance:')
        userAccountNumber = int(input('Pleae enter your account number: '))
        userPassword = input('Please enter the password: ')
        theBalance = getBalance(userAccountNumber, userPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)

    elif action == 'd':
        print('Deposit:')
        userAccountNumber = int(input('Pleae enter your account number: '))
        userDepositAmount = input('Please enter amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter the password: ')
        newBalance = deposit(userAccountNumber, userDepositAmount, userPassword)

        if newBalance is not None:
            print('Your balance is:', newBalance)

    elif action == 'n':
        print('New Account:')
        userName = input('What is your name? ')
        userAccountNumber = int(input('Please enter your account number: '))
        userStartingAmount = int(input('What is the amount of your intial deposit? '))
        userPassword = input('What password would you like to use for ' \
        'this account? ')
        userAccountNumber = len(accountsList)
        newAccount(userName, userStartingAmount, userPassword)
        print('Your new account number is:', userAccountNumber)
            
    elif action == 's': # отображаем
        userAccountNumber = int(input('Pleae enter your account number: '))
        show(userAccountNumber)
    
    elif action == 'q':
        break

    elif action == 'w':
        print('Withdraw:')
        userAccountNumber = int(input('Pleae enter your account number: '))
        userWithdrawAmount = input('Please enter the amount to withdraw: ')
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input('Please enter the password: ')
        newBalance = withdraw(userAccountNumber, userWithdrawAmount, userPassword)

        if newBalance is not None:
            print('Your balance is:', newBalance)

print('Done')