def get_amount():
    while True :
        try:
            return float(input(" bill amount:"))
        except ValueError :
            print(" invalid amount")
def get_percentage():
    while True:
        try :
            tip= float(input(" tip percentage (%):"))
            return tip/100
        except ValueError:
            print(" invalid percentage ")

def calculate_Tip(amount,percentage):
    return amount*percentage


def totalppl():
    while True:
        try:
           return int(input(" total no. of people:"))
           if n<=0:
             print("it should be positive")
           else:
            return n
            
        except ValueError:
            print(" enter a valid no.!")

    

def main() :
    
    amount=get_amount()
    percentage = get_percentage()
    tip = calculate_Tip(amount , percentage)
    
    total = amount + tip

    people =totalppl()
    


    
    print(f"tip : ru{tip:.2f}")
    print(f"total:ru{total:.2f}")
    print(f"each person contro:{total/people:.2f}")
     
main()
