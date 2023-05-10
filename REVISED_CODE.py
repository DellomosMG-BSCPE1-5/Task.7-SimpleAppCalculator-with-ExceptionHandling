#Create a Simple App Calculator
#MODULES USED
while True:
    from art import *
    from colorama import Fore, Back, Style
    from pyboxen import boxen
    from rich.progress import track
    from time import sleep
    from rich.console import Console

    #TITLE
    program_title = text2art("CALCULATE  IT!", font='tarty1', chr_ignore=True)
    print(Fore.CYAN + program_title)

    #HEADER
    print(
            boxen(
                "  Welcome to Calculate it! A calculator for every need, accuracy at your fingertips.  ",
                color="cyan",
            )
        )

    #MAKE A MENU for the 4 arithmetic operations namely addition, subtraction, multiplication, and division
    def menu ():
        print(Fore.CYAN + "OPTIONS:", Fore.WHITE + "\n\n[1] Addition, \n[2] Subtraction, \n[3] Multiplication, \n[4] Division")
        
        #TRY. Ask the user to choose one of the four math operations: Addition, Subtraction, Multiplication, and Division.        
        try:
            print(Fore.LIGHTCYAN_EX + Style.NORMAL + "\nKindly enter the number that corresponds to the operation you want to perform: ", end = "")
            option_number = float(input(Fore.WHITE + ""))
        #EXECUTE EXCEPT BLOCK if the user enter a non-numeric character.
        except ValueError:
            print(
                    boxen(
                        "  Invalid Input. Please enter a numeric character from 1-4 only. ",
                        color="cyan",
                        padding = (0,7,0,7)
                    )
                )
            menu()

        #EXECUTE ELSE BLOCK if the user enter a numeric character.
        else:
            def calculate():
                #If the user's choice is one of the ones in the menu:
                if 0 < option_number <= 4:    
                    #THEN ask the user to input two numbers. 
                    number_1 = float(input("\nEnter first number: "))
                    number_2 = float(input("Enter second number: "))

                    #EXTRA: Loading effect. (Just a decoration)
                    print("\n")
                    def processing_data():
                        sleep(0.01)
                    for _ in track(range(100), description='[blue]Processing data'):
                        processing_data()

                    #IF the user type 1 (Addition):
                    if option_number == 1:
                        #Perform operation and display the Result 
                        print("\n", Fore.BLUE + "=" * 105)
                        console = Console()
                        console.print("\n", "[cyan]The sum is[cyan]: ", number_1 + number_2)

                    #IF the user type 2 (Subtraction):
                    elif option_number == 2:
                        #Perform operation and display the Result 
                        print("\n", Fore.BLUE + "=" * 105)
                        console = Console()
                        console.print("\n", "[cyan]The difference is[cyan]: ", number_1 - number_2)

                    #IF the user type 3 (Multiplication):
                    elif option_number == 3:
                        #Perform operation and display the Result 
                        print("\n", Fore.BLUE + "=" * 105)
                        console = Console()
                        console.print("\n", "[cyan]The product is[cyan]: ", number_1 * number_2)

                    #ELSE, IF the user type 4 (Division):
                    elif option_number == 4:
                        #Perform the operation 
                        try:
                            quotient = number_1 / number_2
                            print("\n", Fore.BLUE + "=" * 105)
                            console = Console()
                            console.print("\n", "[cyan]The product is[cyan]: ", quotient)
                        #EXECUTE THE EXCEPT BLOCK incase the user enter a zero (0) in the second number.
                        except ZeroDivisionError:
                            print(
                                    boxen(
                                        "ZeroDivisionError: Your second number cannot be 0. Please enter another number.",
                                        color="cyan",
                                    )
                                )
                            calculate()

                #ELSE, IF the user's choice is greater than 4, tell to enter an appropriate value.
                else:
                    print(
                            boxen(
                                "You have not typed a valid number. Please enter a number that is from the menu (1-4).",
                                color="cyan",
                            )
                        )
                    menu()


            calculate()
    menu()

    #Ask if user wants to run the program again.
    check = input("\nDo you want to run the program again? Type Y to restart or press another key to quit: ")  # Asking the user if he/she wants to try/start again.
    #IF user typed "y", go back to the top.
    if check.upper() == "Y":  
        continue
    #ELSE, if the user press other key, quit the program.
    print("\n", Fore.BLUE + "=" * 105)
    print(Fore.CYAN + "\nThank you for using this program! Have a Nice Day!\n")
    break

