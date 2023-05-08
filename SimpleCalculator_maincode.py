#Create a Simple App Calculator

#Make a menu for the options (Addition, Subtraction, Multiplication, Division)
operation_options = {
    1: "Addition",
    2: "Subtraction",
    3: "Multiplication",
    4: "Division",
}

def print_options():
    print("Kindly enter the number that corresponds to the operation you would like to complete...\n")
    for key in operation_options.keys():
        print(key, "==", operation_options[key])

print_options()
#Ask the user to choose one of the four math operations: Addition, Subtraction, Multiplication, and Division.

#IF the user chose Addition:
    #THEN ask the user to input two numbers. Can be float and integers.
    #Perform the operation.
    #Display the Result 
#ELIF the user chose subtraction:
    #THEN ask the user to input two numbers. Can be float and integers.
    #Perform the operation.
    #Display the Result 
#ELIF the user chose multiplication:
    #THEN ask the user to input two numbers. Can be float and integers.
    #Perform the operation.
    #Display the Result 
#ELIF the user chose Division:
    #THEN ask the user to input two numbers. Can be float and integers.
    #Perform the operation.
    #Display the Result 
#ELSE
    #Inform the user that he/she inputted a number that was not included in the options

#Ask if user wants another calculation
#IF the answer in "no":
    #THEN end the program
