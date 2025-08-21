m1=float(input("Enter your marks in Internal test-I:"))
m2=float(input("Enter your marks in Internal test-II:"))
m3=float(input("Enter your marks in Internal test-III:"))
low_marks=m1
if m2<low_marks:
    low_marks=m2
if m3<low_marks:
    low_marks=m3
avg=float((m1+m2+m3-low_marks)/2)
print("The best of two tests average among three:",avg)


