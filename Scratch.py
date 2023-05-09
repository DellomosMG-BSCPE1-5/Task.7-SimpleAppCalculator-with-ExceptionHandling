#Create a Simple App Calculator

#Make a menu for the options (Addition, Subtraction, Multiplication, Division)
def Calculator ():
    print("Please select one from the options:")

    print("\n\t[1] Addition")
    print("\t[2] Subtraction")
    print("\t[3] Multiplication")
    print("\t[4] Division")

    #Ask the user to choose one of the four math operations: Addition, Subtraction, Multiplication, and Division.
    try:
        option_number = int(input("\nKindly enter the number that corresponds to the operation you want to perform: "))

        #If the user's choice is one of the ones in the menu:
        if option_number <= 4:
            #Ask the user to input two numbers. Can be float and integers.
            number_1 = float(input("Enter first number: "))
            number_2 = float(input("Enter second number: "))
            
            #IF the user chose Addition:
            if option_number == 1:
                #Display the Result 
                print(number_1 + number_2) 

            #ELIF the user chose subtraction:
            elif option_number == 2:
                #Display the Result
                print(number_1 - number_2) 

            #ELIF the user chose multiplication:
            elif option_number == 3:
                #Display the Result
                print(number_1 * number_2) 

            #ELSE, if the user chose Division:
            else:
                #Perform the operation.
                quotient = number_1 / number_2
                #Display the Result 
                print(format(quotient, ".3f"))
        
        #If the user's choice is one of the ones in the menu:
        else:
            print("\nYou have not typed a valid number. Please enter a number from the menu (1-4).\n")
            Calculator()

    except ValueError:
        print("Invalid Input. Please type your number as numeric characters")
        Calculator()
  

#Ask if user wants another calculation
#IF the answer in "no":
#THEN end the program
Calculator()
