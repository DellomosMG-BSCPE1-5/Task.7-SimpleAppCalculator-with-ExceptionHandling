#Create a Simple App Calculator

#Make a menu for the options (Addition, Subtraction, Multiplication, Division)
while True:
    def menu ():
        print("Please select one from the options:")
        print("\n\t[1] Addition")
        print("\t[2] Subtraction")
        print("\t[3] Multiplication")
        print("\t[4] Division")

        #Ask the user to choose one of the four math operations: Addition, Subtraction, Multiplication, and Division.
        try:
            option_number = int(input("\nKindly enter the number that corresponds to the operation you want to perform: "))
        #If the user enter a character other than numeric
        except ValueError:
            print("\nInvalid Input. Please type your number as numeric character\n")
            menu()
        #else
        else:
            def calculate():
                #If the user's choice is one of the ones in the menu:
                if 0 < option_number <= 4:
                    #Then ask the user to input two numbers. Can be float and integers.
                    number_1 = float(input("Enter first number: "))
                    number_2 = float(input("Enter second number: "))
                    
                    #IF the user chose type 1 (Addition):
                    if option_number == 1:
                        #Perform operation and display the Result 
                        print(number_1 + number_2) 
                    #ELIF the user chose subtraction:
                    elif option_number == 2:
                        #Perform operation and display the Result 
                        print(number_1 - number_2) 
                    #ELIF the user chose multiplication:
                    elif option_number == 3:
                        #Perform operation and display the Result 
                        print(number_1 * number_2) 
                    #ELSE, if the user chose Division:
                    else: 
                        try:
                            #Perform the operation.
                            quotient = number_1 / number_2
                            #Display teh result
                            print(format(quotient, ".3f"))
                        #except there's a ZeroDivisionError
                        except ZeroDivisionError:
                            print("Zero Division Error: Second number cannot be 0. Please enter again. ")
                            calculate()
                                            
                #If the user's choice is not one from the menu:
                else:
                    print("\nYou have not typed a valid number. Please enter a number that is from the menu (1-4).\n")
                    menu()
            
            calculate()
    menu()
    
    #Ask if user wants another calculation
    check = input("\nDo you want to run the program again? Type Y to restart or press another key to quit: ")  # Asking the user if he/she wants to try/start again.
    if check.upper() == "Y":  # go back to the top
        continue
    #IF the answer in "no":
    print("Thank you for using this program!")
    #THEN end the program
    break

