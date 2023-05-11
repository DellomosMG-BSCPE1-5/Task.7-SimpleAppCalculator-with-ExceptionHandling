#Create a Simple App Calculator
#modules
from art import *
from colorama import Fore, Back, Style
from pyboxen import boxen
from rich.progress import track
from time import sleep
from rich.console import Console

def introductions():
    #TITLE
    program_title = text2art("CALCULATE  IT!", font='tarty1', chr_ignore=True)
    print(Fore.CYAN + program_title)

    #HEADER
    print('\n' +
            boxen(
                "  Welcome to Calculate it! A calculator for every need, accuracy at your fingertips.  ",
                color="cyan",
            )
        )

def calculator():
    #create a menu
    print(Fore.CYAN + Style.BRIGHT + "\nOPTIONS:", Fore.WHITE + Style.NORMAL + "\n[1] Addition, \n[2] Subtraction, \n[3] Multiplication, \n[4] Division\n")
    
    try:
        #Ask the user to choose one of the four math operations: Addition, Subtraction, Multiplication, and Division.
        global option_number
        print(Fore.LIGHTCYAN_EX + Style.NORMAL + "\nKindly enter the number that corresponds to the operation you want to perform: ", end = "")
        option_number = float(input(Fore.WHITE + ""))     

    #If the user enter a character other than numeric   
    except ValueError as ERROR:
            print('\n' +
                    boxen(
                        "  Invalid Input. Please enter a numeric character from 1-4 only. ",
                        color="cyan",
                        padding = (0,7,0,7)
                    )
                )      
            calculator() 

    #if the user's choice is one of the ones in the menu:        
    if 0 < option_number <= 4:
        #then ask the user to input two numbers. Can be float and integers.
        first_number = float(input("\n\tEnter first number: "))
        second_number = float(input("\tEnter second number: "))  

        #EXTRA: Loading effect. (Just a decoration)
        print("\n", Fore.BLUE + "=" * 105)
        def processing_data():
            sleep(0.01)
        for _ in track(range(100), description='[blue]Processing data'):
            processing_data()
        print(Fore.BLUE + "=" * 105)

        #if the user chose Addition:
        if option_number == 1:
            #Perform operation and display the result 
            console = Console()
            console.print("\n", "[cyan]The sum is[cyan]: ", first_number + second_number)

        #if the user chose Subtraction:
        elif option_number == 2:
            #perform operation and display the result 
            console = Console()
            console.print("\n", "[cyan]The difference is[cyan]: ", first_number - second_number)

        #if the user chose Multiplication:
        elif option_number == 3:
            #Perform operation and display the result 
            console = Console()
            console.print("\n", "[cyan]The product is[cyan]: ", first_number * second_number)

        #if the user chose Division:
        else:
            try: 
                #Perform the operation.
                quotient = first_number / second_number
                #Display the result
                console = Console()
                console.print("\n", "[cyan]The quotient is[cyan]: ",  + quotient)

            except ZeroDivisionError:
                print("\n" +
                        boxen(
                            "Zero Division Error: Second number cannot be 0.",
                            color="cyan",
                        )
                    )   
                             
    #If the user's choice is not one from the menu:
    else:
    #then inform the user that his/her input is invalid.
        print("\n" +
                boxen(
                    "You have not typed a valid number. Please enter a number that is from the menu (1-4).",
                    color="cyan",
                )
            )        
        calculator()

while True:
    introductions()
    calculator()
    again = input("\nDo you want to try again? Type Y to restart or press another key to quit: ")  # Asking the user if he/she wants to try/start again.
    #IF user typed "y", go back to the top.
    if again.upper() == "Y":  
        continue
    #ELSE, if the user press other key, quit the program.
    print("\nThank you for using this program! Have a Nice Day!\n")
    break