def check_balance(balance) :
    print(f"your balance is {balance}")

def deposit(balance,history):

    try:
        amount = float(input("how much to deposit?"))
        if amount<=0:
            print(" amount must be positive!")
        else:
            balance += amount
            history.append(f"depostied{amount}")
            print(f"{amount} depositied!")

    except ValueError:
        print("invalid amount !") 
    return balance 
def withdraw(balance,history) :
    try : 
        amount =float(input(" how mucuh to withraw?"))
        if amount > balance:
            print(" insufficient funds!")
        elif amount<=0:
            print(" amount must be positive")
        else :
            balance -= amount
            history.append(f"withdrawn{amount}")

            print(f"{amount} withdrawn!")
    except ValueError:
        print(" invalid amount!")
    return balance       

balance =1000.0
history=[]

while True:


    print("\n--ATM menu--")
    print("1.check balance")
    print("2.deposit")
    print("3.wihtdraw")
    print("4.Transactional history")
    print("5.exit")
    

    choice =input("choose (1-4):")

    if choice =="1":
        check_balance(balance)
    elif choice=="2":
        balance =deposit(balance,history)
    elif choice =="3":
        balance =withdraw(balance,history)
    elif choice =="4":
      if len(history) ==0:
          print(" no transactions yet")
      else:
          print("\n--transaction histpry")
          for item in history:
              print(item)
    elif choice =="5":
        print(" goodbye")
        break
    else:
        print("invalid choice!")