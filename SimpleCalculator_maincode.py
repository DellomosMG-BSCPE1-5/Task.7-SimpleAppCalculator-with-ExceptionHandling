#Create a Simple App Calculator
#Program title
while True:
    from art import *
    from colorama import Fore, Back, Style
    program_title = text2art("CALCULATE  IT!", font='tarty1', chr_ignore=True)
    print(Fore.CYAN + program_title)

    #Header
    from pyboxen import boxen
    print(
            boxen(
                "  Welcome to Calculate it! A calculator for every need, accuracy at your fingertips.  ",
                color="cyan",
            )
        )

    #Make a menu for the options (Addition, Subtraction, Multiplication, Division)
    def menu ():
        options_label = text2art("OPTION: ", font='lilia', chr_ignore=True)
        print(Fore.CYAN + options_label)
        print(Fore.WHITE + "\n\t[1] Addition")
        print("\t[2] Subtraction")
        print("\t[3] Multiplication")
        print("\t[4] Division")

        #Ask the user to choose one of the four math operations: Addition, Subtraction, Multiplication, and Division.
        try:
            print(Fore.LIGHTCYAN_EX + Style.NORMAL + "\nKindly enter the number that corresponds to the operation you want to perform: ", end = "")
            option_number = float(input(Fore.WHITE + ""))
        #If the user enter a character other than numeric
        except ValueError:
            print(
                    boxen(
                        "  !!! Invalid Input. Please type your number as numeric character  ",
                        color="cyan",
                    )
                )
            menu()
        #else
        else:
            def calculate():
                #If the user's choice is one of the ones in the menu:
                if 0 < option_number <= 4:
                    #Then ask the user to input two numbers. Can be float and integers.
                    number_1 = float(input("\n\tEnter first number: "))
                    number_2 = float(input("\tEnter second number: "))
                    
                    #Loading...
                    from rich.progress import track
                    from time import sleep
                    print('\n')
                    def process_data():
                        sleep(0.01)
                    for _ in track(range(100), description='[blue]Processing data'):
                        process_data()

                    #IF the user chose type 1 (Addition):
                    if option_number == 1:
                        #Perform operation and display the Result 
                        from rich.console import Console
                        print("\n")
                        print(Fore.BLUE + "=" * 105)
                        console = Console()
                        console.print("\n", "[cyan]The sum is[cyan]: ", number_1 + number_2)

                    #ELIF the user chose subtraction:
                    elif option_number == 2:
                        #Perform operation and display the Result 
                        from rich.console import Console
                        print("\n")
                        print(Fore.BLUE + "=" * 105)
                        console = Console()
                        console.print("\n", "[cyan]The difference is[cyan]: ", number_1 - number_2)

                    #ELIF the user chose multiplication:
                    elif option_number == 3:
                        #Perform operation and display the Result 
                        from rich.console import Console
                        print("\n")
                        print(Fore.BLUE + "=" * 105)
                        console = Console()
                        console.print("\n", "[cyan]The product is[cyan]: ", number_1 * number_2)

                    #ELSE, if the user chose Division:
                    else: 
                        try:
                            #Perform the operation.
                            quotient = number_1 / number_2
                            #Display teh result
                            from rich.console import Console
                            print("\n")
                            print(Fore.BLUE + "=" * 105)
                            console = Console()
                            console.print("\n", "[cyan]The quotient is[cyan]: ", quotient)

                        #except there's a ZeroDivisionError
                        except ZeroDivisionError:
                            print("\n")
                            print(
                                    boxen(
                                        "  !!! Zero Division Error: Second number cannot be 0. Please enter again.  ",
                                        color="cyan",
                                    )
                                )                            
                            calculate()
                                            
                #If the user's choice is not one from the menu:
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
    
    #Ask if user wants another calculation
    check = input("\nDo you want to run the program again? Type Y to restart or press another key to quit: ")  # Asking the user if he/she wants to try/start again.
    if check.upper() == "Y":  # go back to the top
        continue
    #IF the answer in "no":
    print(Fore.CYAN + "\nThank you for using this program! Have a Nice Day!")
    #THEN end the program
    break

