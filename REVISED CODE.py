#Create a Simple App Calculator

#define a function
def calculator():
    #create a menu
    print("\nOPTION:")
    print("\n\t[1] Addition")
    print("\t[2] Subtraction")
    print("\t[3] Multiplication")
    print("\t[4] Division")

    try:
    #Ask the user to choose one of the four math operations: Addition, Subtraction, Multiplication, and Division.
        option_number = float(input("\nKindly enter the number that corresponds to the operation you want to perform: "))
    #If the user enter a character other than numeric   
    except ValueError as ERROR:
        print("Invalid Input. Please type your number as numeric character.")
        calculator() 

    #if the user's choice is one of the ones in the menu:
    if 0 < option_number <= 4:
        #then ask the user to input two numbers. Can be float and integers.
        first_number = float(input("\n\tEnter first number: "))
        second_number = float(input("\tEnter second number: "))

        #if the user chose Addition:
        if option_number == 1:
            #Perform operation and display the result 
            print(first_number + second_number)
        
        #if the user chose Subtraction:
        elif option_number == 2:
            #perform operation and display the result 
            print(first_number - second_number)
        
        #if the user chose Multiplication:
        elif option_number == 3:
            #Perform operation and display the result 
            print(first_number * second_number)

        #if the user chose Division:
        else:
            #Perform operation and display the result 
            print(first_number / second_number)

#If the user's choice is not one from the menu:
    else:
    #then inform the user that his/her input is invalid.
        print("You have not typed a valid number. Please enter a number that is from the menu (1-4).")

#Ask if user wants another calculation
#IF the answer in "no":
    #THEN end the program
while True:
    calculator()
