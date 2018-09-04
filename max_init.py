''' Design an algorithm that finds the maximum positive 
integer input by a user.  
The user repeatedly inputs numbers until a negative value is entered.'''


# The user inputs a number
# The user continues to input numbers until he puts in a negative value
# Then the maximum number the user put in prints out



# Fill in the missing code
num_int = 0
max_int = 0

while num_int >= 0:
    num_int = int(input("Input a number: "))
    if num_int > max_int:
        max_int = num_int
        

print("The maximum is", max_int)  