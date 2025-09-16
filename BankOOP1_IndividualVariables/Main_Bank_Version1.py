# Тестовая программа, использующая счета
# Версия 1, использующая явные переменные для каждого объекта Account

# Берем весь код из файла класса Account
from Account import *

# создаем два счета
oJoesAccount = Account('Joe', 100, 'JoesPassword')
print('Created an account for Joe')
oMarysAccount = Account('Mary', 12345, 'MarysPassword')
print('Created an account for Mary')
oJoesAccount.show()
oMarysAccount.show()
print()

# вызываем разные методы для разных счетов
print('Calling methods of the two accounts ...')
oJoesAccount.deposit(50, 'JoesPassword')
oMarysAccount.withdraw(345, 'MarysPassword')
oMarysAccount.deposit(100, 'MarysPassword')

# отображаем счета
oJoesAccount.show()
oMarysAccount.show()

# создаем новый счет с информацией от пользователя
print()
userName = input('What is the name for the new user account? ')
userBalance = int(input('What is the starting balance for this account? '))
userPassword = input('What is the password you want to use for this ' \
'account? ')
oNewAccount = Account(userName, userBalance, userPassword)
oNewAccount.show()

# вносим 100 на новый счет пользователя
oNewAccount.deposit(100, userPassword)
userBalance = oNewAccount.getBalance(userPassword)
print()
print('After depositing 100, the user\'s balance is:', userBalance)

# отображаем новый счет
oNewAccount.show()
