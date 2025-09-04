def calculate_total(bill_amount,tax_percent,tip_percent):
    tax=bill_amount*(tax_percent/100)
    tip=bill_amount*(tip_percent/100)
    return bill_amount+tax+tip
def split_bill(total,people):
    return total/people
amount=float(input("Enter Bill amount:"))
tax=float(input("Enter Tax percentage:"))
tip=float(input("Enter Tip percentage:"))
people=int(input("Number of people to split:"))

total=calculate_total(amount,tax,tip)
each=split_bill(total,people)

print(f"\nTotal Bill:Rs.{total:.2f}")
print(f"Each person should pay:Rs.{each:.2f}")
