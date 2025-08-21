import sys
correct_pin="1234"
balance=5000
pin=input("Enter your ATM PIN:")
if pin!=correct_pin:
    print("Invalid Pin.  Exiting...")
    sys.exit()
withdraw=float(input("Enter amount to withdraw:"))
if withdraw<=0:
    print("Invalid Amount!")
elif withdraw>balance:
    print("Insufficient balance!")
else:
    balance -= withdraw
    print("Withdrawal Successful.  Remaining balance:",balance)
               
