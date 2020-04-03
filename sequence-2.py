#Using the "for loop", This program will print out each even number from 0 - 99.

#Lets define number.
number = 0

#create a "for" loop that loop through each number starting at 0 and ending at 99.
for number in range(100):

    #create a variable that will only print out the even numbers from 0 to 99 using the modulo.
    is_even = number % 2 == 0
    
    #Using the "if" statement, print out all even numbers.
    if is_even:
        
        #Print even numbers.
        print(number)


