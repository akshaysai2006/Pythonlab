counter = 10
def local_increment():
    counter = 10  
    counter += 1
    print("Inside function(local) :", counter)
local_increment()
print("Outside function(global) :", counter)
