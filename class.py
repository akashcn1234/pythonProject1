class Bank:
  def __init__(self,accno,name,type,bal):
    self.accno=accno
    self.name=name
    self.type=type
    self.bal=bal
  def deposit(self,amount):
    self.bal=self.bal+amount
    print("amount deposited  successfully")
    return self.bal
  def withdraw(self,amount):
    if amount>self.bal:
       print ("insufficient balance")
       return self.bal
    else:
      self.bal=self.bal_amount
      print("amount withdrawwed successfully")
b=Bank(1001,"abhi","savings",3000)
damount=float(input("enter the amount to be  deposited:"))
print("account balance:",b.deposit(damount))
wamount=float(input("enter the amount to be withdraw:"))
print("accont balance:",b.withdraw(wamount))
