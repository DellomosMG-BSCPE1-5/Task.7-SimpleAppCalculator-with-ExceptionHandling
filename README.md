# CMPE 103 OBJECT-ORIENTED PROGRAMMING
```
LAB EXERCISE No. 7 – Simple Calculator
```

## Task Instruction:
1.  The application will ask the user to choose one of the 
      four math operations (Addition, Subtraction, Multiplication and Division)
2.  The application will ask the user for two numbers
3.  Display the result
4. The application will ask if the user wants to try again or not.
5. If yes, repeat Step 1.
6. If no, Display “Thank you!” and the program will exit 
7. Use Python Function and appropriate Exceptions to capture errors during   
    runtime.

## The Main Code
### Modules Used
Kindly install the following modules for the program to work properly.
* Pyfiglet
* colorama

### How it works
The main code will run in the terminal where the user will input the required texts such as the date and his/her entry for the day. Then, these inputs will be forward directly to the text file named mylife.txt. After that, the program will ask the user if he/she wants to enter another text again. If the user typed "yes", the program will start again and repeat the process. The new text entered will append to mylife.txt without removing and replacing the first text entered by the user. On the other hand, if the user answered "no", and doesn't want to add another text, then the program will stop. 

### The Main Code contains the following:
* Defines a function 
* While Loop
* If-Else Statements
* open() function
* write() method
* upper() method
* string concatenation 

## GUI Involved Program
### Module/s Used 
Kindly install the following modules for the program to work properly.
* Tkinter

### How it works
Running this program in the terminal, a small window will appear. Note! do not expand the window for better experience. In this window, you will see two entry boxes and three buttons. In these entry boxes, the user will input their entries. Clicking the "Submit" button, the entries will be append/write/forwarded to the mylife.txt. Clicking the "I want to write more" button, on the other hand, the previous entry will be cleared and the entry boxes are ready for filling out again. If the user wants to exit the window, just click the "Quit" button.


### Links and Sources
* https://youtu.be/CKeFRDXYwcA
* https://www.geeksforgeeks.org/how-to-close-a-tkinter-window-with-a-button/
* https://pythonexamples.org/python-tkinter-window-background-color/#5
* https://github.com/codefirstio/modern-todo-tkinter/blob/main/gui.py
