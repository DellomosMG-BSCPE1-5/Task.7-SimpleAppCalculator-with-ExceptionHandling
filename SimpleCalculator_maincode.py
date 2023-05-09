#Create a Simple App Calculator

#Make a menu for the options (Addition, Subtraction, Multiplication, Division)
def Mainmenu ():
    print("Please select one from the options:")

    print("\n\t[1] Addition")
    print("\t[2] Subtraction")
    print("\t[3] Multiplication")
    print("\t[4] Division")

def Calculations ():
        option_number = int(input("\nKindly enter the number that corresponds to the operation you want to perform: "))
#IF the user chose Addition:
        if option_number == 1:
        #THEN ask the user to input two numbers. Can be float and integers.
            number_1 = float(input("Enter first number: "))
            number_2 = float(input("Enter second number: "))
        #Perform the operation.
            sum = number_1 + number_2
        #Display the Result 
            print(sum) 

    #ELIF the user chose subtraction:
        elif option_number == 2:
        #THEN ask the user to input two numbers. Can be float and integers.
            number_1 = float(input("Enter first number: "))
            number_2 = float(input("Enter second number: "))
        #Perform the operation.
            difference = number_1 - number_2
        #Display the Result 
            print(difference)

    #ELIF the user chose multiplication:
        elif option_number == 3:
        #THEN ask the user to input two numbers. Can be float and integers.
            number_1 = float(input("Enter first number: "))
            number_2 = float(input("Enter second number: "))
        #Perform the operation.
            product = number_1 * number_2
        #Display the Result 
            print(product)
            
    #ELIF the user chose Division:
        #THEN ask the user to input two numbers. Can be float and integers.
        #Perform the operation.
        #Display the Result 
    #ELSE
        #Inform the user that he/she inputted a number that was not included in the options

#Ask if user wants another calculation
#IF the answer in "no":
    #THEN end the program
Mainmenu()
Calculations()