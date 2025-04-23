import unittest
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase): #this is a test framework used to test the bank account the bank_account.py code

    def setUp(self): #executes before every test, this sets the balance to 100
        self.account = BankAccount(100)

    def tearDown(self): #executes after every test, resets the balance
        self.account = None

    def test_initial_balance(self): #Checks the inital balance is 100
        self.assertEqual(self.account.balance, 100)


    #Deposit test functions

    def test_deposit_positive_amount(self): #Checks if the deposit function works
        self.account.deposit(-50)
        self.assertEqual(self.account.balance, 150)
    
    def test_deposit_negative_amount(self):  #Checks if the negative ValueError works
        with self.assertRaises(ValueError):
            self.account.deposit(-40)
    
    #Withdraw test functions

    def test_withdraw_sufficient_funds(self): #Checks if withdrawal function works
        self.account.withdraw(30)
        self.assertEqual(self.account.balance, 70)

    def test_withdraw_insufficient_funds(self): #Checks if ValueError is raised to avoid withdrawing excesive amounts
        with self.assertRaises(ValueError):
            self.account.withdraw(200)

    def test_withdraw_zero_amount(self): #Checks if 0 is withdrawn, if so ValueError is shown
        with self.assertRaises(ValueError):
            self.account.withdraw(0)

    def test_withdraw_negative_amount(self): #Checks if a negative amount is withdrawn, if so ValueError is shown
        with self.assertRaises(ValueError):
            self.account.withdraw(-50)


if __name__ == '__main__': #checks if the test file is being run
    unittest.main()