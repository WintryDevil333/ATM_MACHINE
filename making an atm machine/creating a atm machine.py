import time
def print_english():
    print("Please insert Your CARD")
    
language = input("Choose a language(only english) : ")

if language.lower() == "english":
    print_english()
else:
    print("Invalid language choice.please try again")

time.sleep(3)

password = 9078

balance = 15000

while True:
  if language=='english':
            print("please do not remove your card.leave your card inserted during transaction")
            time.sleep(3)
                    
  
  break

pin=int(input("please enter your 4 digit PIN number:  "))
if pin == password:

     
     

      while True:  

        print("""
                      ********  MENU  ********
                      
			1 == check balance
			2 == withdraw money
			3 == deposit money
			4 == exit
			"""
              )

        try:    
            option = int(input("Please enter your choice "))
        except:
            print("Please enter valid option")
          
        if option == 1:
            print("----------------------------------------------------")
            print(f"Your current balance is {balance}")
            
                                     
        if option == 2:

            withdraw_amount = int(input("please enter withdraw_amount "))
            
            print("----------------------------------------------------")
            
            balance = balance - withdraw_amount

            print(f"transaction processing")

            time.sleep(3)

            print("----------------------------------------------------")

            print(f"{withdraw_amount} is debited from your account")

            print(f"your updated balance is {balance}")

            
        if option == 3:

            deposit_amount = int(input("please enter deposit_amount"))

            balance = balance + deposit_amount

            print("----------------------------------------------------")

            print("please...wait a moment")

            time.sleep(3)

            print("----------------------------------------------------")

            print(f"{deposit_amount} is credited to your account")

            print(f"your updated balance is {balance}")



        if option == 4:
            print("THANK YOU FOR VISITING OUR ATM.....SEE YOU SOON")

            break

else:
    print("wrong pin Please try again")



