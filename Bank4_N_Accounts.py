# Без ООП
# Банк. Версия 4
# Любое количество счетов - со списками
accountNameList = []
accountBalanceList = []
accountPasswordList = []

def newAccount(name, balance, password):
    global accountNameList, accountBalanceList, accountPasswordList
    accountNameList.append(name)
    accountBalanceList.append(balance)
    accountPasswordList.append(password)

def show(accountNumber):
    global accountNameList, accountBalanceList, accountPasswordList
    print('Account', accountNumber)
    print('     Name', accountNameList[accountNumber])
    print('     Balance', accountBalanceList[accountNumber])
    print('     Password:', accountPasswordList[accountNumber])
    print()
    
def getBalance(accountNumber, password):
    global accountNameList, accountBalanceList, accountPasswordList
    if password != accountPasswordList[accountNumber]:
        print('Incorrect password')
        return None
    return accountBalanceList[accountNumber]

def deposit(accountNumber, amountToDeposit, password):
    global accountNameList, accountBalanceList, accountPasswordList
    if amountToDeposit < 0:
        print('You connot deposit a negative amount!')
        return None
    
    if password != accountPasswordList[accountNumber]:
        print('Incorrect password')
        return None

    accountBalanceList[accountNumber] = accountBalanceList[accountNumber] + amountToDeposit
    return accountBalanceList[accountNumber]

def withdraw(accountNumber, amountToWithdraw, password):
    global accountNameList, accountBalanceList, accountPasswordList
    if amountToWithdraw < 0:
        print('You cannot withdraw a negative amount')
        return None
    
    if password != accountPasswordList[accountNumber]:
        print('Incorrect password')
        return None
    
    if amountToWithdraw > accountBalanceList[accountNumber]:
        print('You cannot withdraw more than you have in your account')
        return None
    
    accountBalanceList[accountNumber] = accountBalanceList[accountNumber] - amountToWithdraw
    return accountBalanceList[accountNumber]

print('Joe`s account is account number:', len(accountNameList))
newAccount('Joe', 100, 'soup')

print('Mary`s account is account number:', len(accountNameList))
newAccount('Mary', 12345, 'nuts')

while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
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