import multiprocessing
import random
import logging
from dataclasses import dataclass

NATIONAL_ID_LENGTH = 6
PLN_TO_EUR_RATE = 0.22

logging.basicConfig(format='%(message)s',level=logging.INFO)

class Bank:
  def __init__(self, name, capital):
    self.name = name
    self.capital = capital

  def __repr__(self):
    return "{} (Initial capital: {} PLN = {} EUR)".format(self.name, self.capital, self.pln_to_eur(self.capital))

  @classmethod
  def fake(cls):
    return cls("FakeBank {}".format(random.randint(1,9)), random.randint(10000,20000))

  @classmethod
  def none(cls):
    return cls("None", 0)

  @staticmethod
  def pln_to_eur(amount_pln):
    return amount_pln * PLN_TO_EUR_RATE

class Client:
  def __init__(self, first_name, last_name, national_id, bank, balance):
    self.first_name = first_name
    self.last_name = last_name
    self.national_id = national_id
    self.bank = bank
    self.balance = balance
  
  def __str__(self):
    return "Client {} {} has a balance of {} PLN at bank \"{}\"".format(self.last_name, self.first_name, self.balance, self.bank.name)

  @property
  def national_id(self):
    return self.__national_id
  
  @national_id.setter
  def national_id(self, national_id):
    if len(national_id) != NATIONAL_ID_LENGTH:
      # should raise exception but it looks bad in the output & the program doesn't finish
      logging.error("National ID has to have length of {}.".format(NATIONAL_ID_LENGTH))
    else:
      self.__national_id = national_id

  def delete_bank_account(self):
    if self.balance < 0:
      logging.error("Account of {} {} at {} cannot be deleted because it has a negative balance ({} PLN).".format(self.last_name, self.first_name, self.bank.name, self.balance))
      return False
    else:
      self.bank = Bank.none()
      self.balance = 0
      return True

class Transaction:
  def __init__(self, amount, sender, recepient):
    self.amount = amount
    self.sender = sender
    self.recepient = recepient

  def transfer(self):
    if self.sender.balance - self.amount > 0:
      self.sender.balance -= self.amount
      self.recepient.balance += self.amount
      return True
    else:
      return False

  # sender == recepient for cash input & withdrawl
  def cash_input(self):
    self.recepient.balance += self.amount
    return True
  
  def cash_withdrawal(self):
    if self.recepient.balance - self.amount <= 0:
      return False
    else:
      self.recepient.balance -= self.amount
      return True

@dataclass
class ATM:
    name: str
    bank: Bank
    money_reserve: float
    in_service: bool

    def destroy(self):
        self.in_service = False

def bank_worker(bank, clients):
<<<<<<< HEAD
  logging.info("Process started for bank: {}".format(bank.name))
=======
  logging.info("\nProcess started for bank: {}".format(bank.name))
>>>>>>> 6530e9a1d17dcf4ed54ac177fb93ef2bca01efc4

  client1, client2 = random.sample(clients, 2)

  t = Transaction(500, client1, client2)
  if t.transfer():
    logging.info("{} PLN was successfully transferred from {} {} to {} {}.".format(t.amount, t.sender.last_name, t.sender.first_name, t.recepient.last_name, t.recepient.first_name))
  else:
    logging.info("Sender {} {} does not have adequate funds to complete the transaction to recepient {} {}!".format(t.sender.last_name, t.sender.first_name, t.recepient.last_name, t.recepient.first_name))
  logging.info(client2)

  t = Transaction(50, client2, client1)
  if t.transfer():
    logging.info("{} PLN was successfully transferred from {} {} to {} {}.".format(t.amount, t.sender.last_name, t.sender.first_name, t.recepient.last_name, t.recepient.first_name))
  else:
    logging.info("Sender {} {} does not have adequate funds to complete the transaction to recepient {} {}!".format(t.sender.last_name, t.sender.first_name, t.recepient.last_name, t.recepient.first_name))
  logging.info(client2)

  t = Transaction(25, client2, client2)
<<<<<<< HEAD
  if t.cash_withdrawal():
=======
  if t.cash_withdrawl():
>>>>>>> 6530e9a1d17dcf4ed54ac177fb93ef2bca01efc4
    logging.info("Client {} {} has made a withdrawl of {} PLN from his account and now has a balance of {} PLN".format(t.recepient.last_name, t.recepient.first_name, t.amount, t.recepient.balance))
  else:
    logging.info("Client {} {} does not have adequate funds to make cash withdrawl.".format(t.recepient.last_name, t.recepient.first_name))
  logging.info(client2)

  t = Transaction(75, client2, client2)
  if t.cash_input():
        logging.info("Client {} {} has inputted {} PLN to their account at bank \"{}\"".format(t.recepient.last_name, t.recepient.first_name, t.amount, t.recepient.bank.name))
  logging.info(client2)

  t = Transaction(50, client2, client2)
<<<<<<< HEAD
  if t.cash_withdrawal():
=======
  if t.cash_withdrawl():
>>>>>>> 6530e9a1d17dcf4ed54ac177fb93ef2bca01efc4
    logging.info("Client {} {} has made a withdrawl of {} PLN from his account and now has a balance of {} PLN".format(t.recepient.last_name, t.recepient.first_name, t.amount, t.recepient.balance))
  else:
    logging.info("Client {} {} does not have adequate funds to make cash withdrawl.".format(t.recepient.last_name, t.recepient.first_name))
  logging.info(client2)
  
  return

if __name__ == "__main__":
  bank1 = Bank("Bank Pekao", 20000)
  bank2 = Bank("Bank Polska", 100000)
  bank3 = Bank("Intesa Sanpaolo", 30000)

  client1 = Client("Zeljko", "Joksimovic", "123456", bank1, 200)
  client2 = Client("Aco", "Vucic", "987654", bank1, 100)
  client3 = Client("Palma", "Markovic", "987554", bank2, 200)
  client4 = Client("Mile", "Banderas", "887654", bank2, 300)
  client5 = Client("Andrej", "Plenky", "985554", bank2, 150)
  client6 = Client("Gogo", "Njojo", "933654", bank3, 50)
  client7 = Client("Emina", "Hodzic", "984354", bank1, 120)
  client8 = Client("Ferdinand", "Porsche", "987650", bank3, 0)
  client9 = Client("Ivan", "Horvat", "127654", bank2, 20)
  client10 = Client("Joakim", "Hrast", "986704", bank3, 100)
  client11 = Client("Hesus", "Fernandez", "907654", bank2, 160)
  client12 = Client("Lee", "Miller", "988254", bank1, 250)

  bank1_clients = [client1, client2, client7, client12]
  bank2_clients = [client3, client4, client5, client9, client11]
  bank3_clients = [client6, client8, client10]

  p1 = multiprocessing.Process(target=bank_worker, args=(bank1, bank1_clients,))
  p1.start()
  p2 = multiprocessing.Process(target=bank_worker, args=(bank2, bank2_clients,))
  p2.start()
  p3 = multiprocessing.Process(target=bank_worker, args=(bank3, bank3_clients,))
  p3.start()

<<<<<<< HEAD
  logging.info(client2)
  client2.bank = bank2
  logging.info(client2)
=======
  logging.info("\n")
  logging.info(client2)
  client2.bank = bank2
  logging.info(client2)
  logging.info("\n")
>>>>>>> 6530e9a1d17dcf4ed54ac177fb93ef2bca01efc4

  client2.national_id = "22"

  bank4 = Bank.fake()
  logging.info(bank4)

  client2.balance = -1
  logging.info(client2)
  client2.delete_bank_account()
  logging.info(client2)

  atm1 = ATM("ATM01", bank1, 100, True)
  atm1.destroy()
  logging.info(atm1)