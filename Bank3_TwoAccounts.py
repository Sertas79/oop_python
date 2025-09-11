# Без ООП
# Банк. Версия 3
# Два счета

account0Name = ''
account0Balance = 0
account0Password = ''
account1Name = ''
account1Balance = 0
account1Password = ''
nAccount = 0
def newAccount(accountNumber, name, balance, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password
    if nAccount == 0:
        account0Name = name
        account0Balance = balance
        account0Password = password
    if nAccount == 1:
        account1Name = name
        account1Balance = balance
        account1Password = password

def show():
    global account0Name, account0Balance, account0Passwordb
    global account1Name, account1Balance, account1Password
    if account0Name != '':
        print('Account 0')
        print('     Name', account0Name)
        print('     Balance', account0Balance)
        print('     Password:', account0Password)
        print()
    if account1Name != '':
        print('Account 1')
        print('     Name', account1Name)
        print('     Balance', account1Balance)
        print('     Password:', account1Password)
        print()

def getBalance(accountNumber, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password
    if accountNumber == 0:
        if password != account0Password:
            print('Incorrect password')
            return None
        return account0Balance
    if accountNumber == 1:
        if password != account1Password:
            print('Incorrect password')
            return None
        return account1Balance
    
def deposit(accountNumber, amountToDeposit, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password
    if accountNumber == 0:
        if amountToDeposit < 0:
            print('You connot deposit a negative amount!')
            return None
        
        if password != account0Password:
            print('Incorrect password')
            return None

        account0Balance = account0Balance + amountToDeposit
        return account0Balance
    if accountNumber == 1:
        if amountToDeposit < 0:
            print('You connot deposit a negative amount!')
            return None
        
        if password != account1Password:
            print('Incorrect password')
            return None

        account1Balance = account1Balance + amountToDeposit
        return account1Balance
    
def withdraw(accountNumber, amountToWithdraw, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password
    if accountNumber == 0:
        if amountToWithdraw < 0:
            print('You cannot withdraw a negative amount')
            return None
        
        if password != account0Password:
            print('Incorrect password')
            return None
        
        if amountToWithdraw > account0Balance:
            print('You cannot withdraw more than you have in your account')
            return None
        
        account0Balance = account0Balance - amountToWithdraw
        return account0Balance
    if accountNumber == 1:
        if amountToWithdraw < 0:
            print('You cannot withdraw a negative amount')
            return None
        
        if password != account1Password:
            print('Incorrect password')
            return None
        
        if amountToWithdraw > account1Balance:
            print('You cannot withdraw more than you have in your account')
            return None
        
        account1Balance = account1Balance - amountToWithdraw
        return account1Balance
    
newAccount(nAccount, 'Joe', 100, 'soup') # создаем аккаунт
nAccount += 1
newAccount(nAccount, 'Kazak', 1000, 'sou') # создаем аккаунт

while True:
    print()
    print('Type b to get the balance')
    print('Type d to make a deposit')
    print('Type n to create a new account')
    print('Type w to make a withdrawal')
    print('Type s to show all accounts')
    print('Type q to quit')
    print()

    action = input('What do you want to do? ')
    action = action.lower()  # force lowercase
    action = action[0]  # just use first letter
    print()
    
    if action == 'b':
        print('Get Balance:')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userPassword = input('Please enter the password: ')
        theBalance = getBalance(userAccountNumber, userPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)

    elif action == 'd':
        print('Deposit:')
        userAccountNumber= input('Please enter the account number: ')
        userAccountNumber = int(userAccountNumber)
        userDepositAmount = input('Please enter amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter the password: ')
        newBalance = deposit(userAccountNumber, userDepositAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance)
        
    elif action == 'n':
        print('New Account:')
        userName = input('What is your name? ')
        userStartingAmount = input('How much money to have to start you account with? ')
        userStartingAmount = int(userStartingAmount)
        userPassword = input('What password would you like to use for this account? ')

        newAccount(nAccounts, userName, userStartingAmount, userPassword)
        print('Your new account number is:', nAccounts)
        nAccounts = nAccounts + 1

    elif action == 's':   #show all
        print('Show:')
        show()

    elif action == 'q':
        break

    elif action == 'w':
        print('Withdraw:')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userWithdrawAmount = input('Please enter the amount to withdraw: ')
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input('Please enter the password: ')
 
        newBalance = withdraw(userAccountNumber, userWithdrawAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance)
        
print('Done')
