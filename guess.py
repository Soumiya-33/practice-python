import random 

secret =random.randint(1,10)
attempts =0

while True :
    try:
        guess = int(input(" guess the no.? "))
    except ValueError:
      print(" its an invalid no.")
      continue

    attempts += 1
    if guess < secret:
        print("No. too low")

    elif guess > secret:
        print("Its too high")

    else:
        print(f"You got the right no. in {attempts}!")
        break
 

   