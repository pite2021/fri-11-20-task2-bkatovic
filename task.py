class Bank:
  def __init__(self, name, balance):
    self.name = name
    self.balance = balance

  def __str__(self):
    return "The \"{}\" bank has a capital of {} polish zloty".format(self.name, self.balance)

class Client:
  def __init__(self, first_name, last_name, national_id, bank, balance):
    self.first_name = first_name
    self.last_name = last_name
    self.national_id = national_id
    self.bank = bank
    self.balance = balance

  def __str__(self):
    return "Client {} {} has a balance of {} PLN at bank \"{}\"".format(self.last_name, self.first_name, self.balance, self.bank.name)

class Transaction:
  def __init__(self, amount, sender, recepient):
    self.amount = amount
    self.sender = sender
    self.recepient = recepient

  def transfer(self):
    if self.sender.balance - self.amount > 0:
      self.sender.balance -= self.amount
      self.recepient.balance += self.amount

      print("{} PLN was successfully transferred from {} {} to {} {}.".format(self.amount, self.sender.last_name, self.sender.first_name, self.recepient.last_name, self.recepient.first_name))
    else:
      print("Sender {} {} does not have adequate funds to complete the transaction to recepient {} {}!".format(self.sender.last_name, self.sender.first_name, self.recepient.last_name, self.recepient.first_name))

  # sender == recepient for cash input & withdrawl
  def cash_input(self):
    self.recepient.balance += self.amount
    print("Client {} {} has inputted {} PLN to their account at bank \"{}\"".format(self.recepient.last_name, self.recepient.first_name, self.amount, self.recepient.bank.name))
  
  def cash_withdrawl(self):
    if self.recepient.balance - self.amount <= 0:
      print("Client {} {} does not have adequate funds to make cash withdrawl.".format(self.recepient.last_name, self.recepient.first_name))
    else:
      self.recepient.balance -= self.amount
      print("Client {} {} has made a withdrawl of {} PLN from his account and now has a balance of {} PLN".format(self.recepient.last_name, self.recepient.first_name, self.amount, self.recepient.balance))

if __name__ == "__main__":
  bank1 = Bank("Bank Pekao", 20000)
  print(bank1)

  client1 = Client("Zeljko", "Joksimovic", 123456, bank1, 200)
  client2 = Client("Aco", "Vucic", 987654, bank1, 100)

  t1 = Transaction(500, client1, client2)
  t1.transfer()

  print(client2)

  t2 = Transaction(50, client2, client1)
  t2.transfer()

  print(client2)

  t3 = Transaction(25, client2, client2)
  t3.cash_withdrawl()

  print(client2)

  t4 = Transaction(75, client2, client2)
  t4.cash_input()

  print(client2)

  t5 = Transaction(50, client2, client2)
  t5.cash_withdrawl()