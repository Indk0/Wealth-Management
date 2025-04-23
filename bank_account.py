#This code is the bank account basic functionality

class BankAccount: 
  def __init__(self, initial_balance=0): #this code defines the initial balance of the bank account through code
    self.balance = initial_balance #this stores the initial balance set by the function

  def deposit(self, amount): #this code is for the deposit functionality
    if amount <= 0: #this checks if the deposite amount is 0 or negative, if so then the following error is shown
      raise ValueError('Deposit amount must be positive')
    self.balance += amount #this code adds the amount being deposited

  def withdraw(self, amount): #this code handles the withdraw functionality
    if amount <= 0: #this checks if the withdrawal amount is 0 or negative, if so the ValueError is shown 
      raise ValueError('Withdrawal amount must be positive')
    if amount > self.balance: #this check is the withdrawal amount is greater than the balance, if it is, the ValueError is shown
      raise ValueError('Insufficient funds')
    self.balance -= amount #this handles the withdrawal, the amount is subtracted from the balance