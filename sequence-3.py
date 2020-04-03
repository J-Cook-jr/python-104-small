#Using the "for loop", This program will print out each odd number from 0 - 99.

#Lets define number.
number = 0

#create a "for" loop that loop through each number starting at 0 and ending at 99.
for number in range(100):

    #create a variable that will only print out the odd numbers from 0 to 99 using the modulo.
    is_odd = number % 2 != 0

    #Using the "if" statement, print out all odd numbers.
    if is_odd:

        #Print odd numbers.
        print(number)
    


