accounts = {}
balances = {}

def is_valid_amount(n):
  try:
      float(n)
  except ValueError:
      return False
  float_n = float(n)
  if float_n > 0 and float(float_n*100).is_integer():
    return True
  return False
      
def create_account(accounts, balances):

  print("Enter Username: ")
  username = input()

  while username in accounts:
    print(username + " username is already in use, please enter a different username.")
    print("Enter Username")
    username = input()

  password = ""
  confirm_password = "1"
  
  print("Enter new Password: ")
  password = hash(input())

  print("Confirm Password: ")
  confirm_password = hash(input())

  while password != confirm_password:
    print("passwords are not the same, please enter password again")
    print("Enter new Password: ")
    password = hash(input())
  
    print("Confirm Password: ")
    confirm_password = hash(input())

  accounts[username] = password
  balances[username] = 0
  return username

def login(accounts):
  print("Enter Username: ")
  username = input()
  print("Enter Password: ")
  password = hash(input())

  while not username in accounts or not accounts[username]==password:
    print("Sorry username/password combo is incorrect, please try again")
    
    print("Enter Username: ")
    username = input()
    print("Enter Password: ")
    password = hash(input())
    
  return username

def deposit(balances):
  print("Enter amount to deposit")
  d = input()
  if is_valid_amount(d):
    balances[username] += float(d)
  else:
    print("You did not enter a valid amount to deposit. You will be bought back to the home screen")

def withdraw(balance):
  print("Enter amount to withdraw: ")
  w = input()
  if is_valid_amount(w) and float(w)<balances[username]:
    balances[username] -= float(w)
  else:
    print("You did not enter a valid amount to withdraw. You will be bought back to the home screen.")
    
while True:
  response = ""

  while not response in {"yes", "no"}:
    print("Do you have an account, type 'yes' if you do, otherwise a 'no': ")
    response = input()

  username = ""
  
  if response == "no":
    username = create_account(accounts, balances)
  if response == "yes":
    username = login(accounts)

  response = ""
  while response != "logout":
    print("You have £" + str(balances[username]) + " in your bank account")
    print("Do you want to deposit or withdraw any cash. Type 'deposit' if you want to deposit, and 'withdraw' to withdraw. Otherwise, type 'logout'")
    response = input()
    
    if response == "deposit":
      deposit(balances)
    if response == "withdraw":
      withdraw(balances)
