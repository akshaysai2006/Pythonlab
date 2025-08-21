marks=int(input("Enter your marks out of hundred:"))
if marks >=90:
    grade="A+"
elif marks >=75:
    grade="A"
elif marks >=60:
    grade="B"
elif marks >=50:
    grade="C"
elif marks>=35:
    grade="D"
else:
    grade="Fail"
print("Your grade is :",grade)
        
