def is_valid(password):
     if len(password) < 8:
          return False
     if not any(c.isupper() for c in password):
          return False
     if not any(c.islower() for c in password):
          return False
     if not any(c.isdigit() for c in password):
          return False
     else:
          return True
     
def main():
     while True:
          password = input(" enter a password : ")
          if is_valid(password):
               print("strong password done")
               break
          else:
               print("weak password , must have:")
               print(" atleast 8 characters")
               print("at least one uppercase ")
               print(" atleast one lowercase ")
               print("should contain atleast one no.")
main()

          
     
