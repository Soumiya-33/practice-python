try:
    a = float(input(" whats a ?"))
    b = float(input(" whats b ?" ))
except ValueError :
    print(" its not the appropriate one ")

else:
    p = input(" whats the operator ?(+,-,%,*,/)")
    if p == "+":
        print(f" the ans is ,{a + b}")
    elif p == "-":
        print(f" the ans is , { a - b}")
    elif p == "%":
        print(f" the ans is , { a % b }")
    elif p == "*" :
        print(f" the ans is , { a * b}")
    elif p =="/" :

        if b == 0:
            print(" this no.  cannot be divided by zero , ans invalid")
        else:
            print(f" the ans is , {a / b}")

    else :
        print( " it is invalid macha ")        


        

                    