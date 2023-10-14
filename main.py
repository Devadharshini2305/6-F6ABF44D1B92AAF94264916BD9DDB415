#Bankaccount class
#with both a despoit() and a withdraw() function
class Bank_Account:

  def __init__(self):
    self.balance = 0
    print("Hello, welcome to Bank Account")

  def deposit(self):
    amount = int(input("Enter the amount to deposit: "))
    self.balance += amount
    print("\namount deposited:", amount)

  def withdraw(self):
    amount = int(input("Enter the amount to withdraw: "))
    if self.balance >= amount:
      self.balance -= amount
      print("\namount withdrawn:", amount)
    else:
      print("\nInsufficient balance")

    def display(self):
      print("\n Account balance=,self.balance")


# Driver code

#creating an object of class
s = Bank_Account()

#calling the functions with that class object
s.deposit()
s.withdraw()
s.display()
