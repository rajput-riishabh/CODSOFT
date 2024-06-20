"""
TASK 2::  CALCULATOR

        Design a simple calculator with basic arithmetic operations.
        Prompt the user to input two numbers and an operation choice.
        Perform the calculation and display the result.
        
"""

# def calculator(operand1,operand2,operation):
#     if operation == '/':
#         return operand1//operand2
#     elif operation == '*':
#         return operand1*operand2
#     elif operation == '%':
#         return operand1%operand2
#     elif operation == '+':
#         return operand1+operand2
#     elif operation == '-':
#         return operand1-operand2
#     else:
#         return "Invalid operation"

# operand1=int(input("Enter digit 1:: "))
# operand2=int(input("Enter digit 2:: "))
# print("operation choice:: /,*,%,+,-")
# operation=input("Enter the arithmetic operation to want to perform:: ")
# print(f"{operand1} {operation} {operand2} = {calculator(operand1,operand2,operation)}")








########################################################################## CALCULATOR APPLICATION #############################################################################################

## Define colors
colb="#292929"
colg="#1CFF20"
colr="#FF0004"
coldg="#474747"



expression="" # empty expresion 

# # create a function to update the result window regularly
def update_result(value):
    global expression
    expression += value
    result.config(text=expression)

# # create a function that will actually performs calculations over the expreesion and catch any error in expression
def calculate_result():
    global expression
    try:
        if expression == "":
            res = "ERROR"
        else:
            res = str(eval(expression))     # the method eval() will evaluate the expression
        result.config(text=res)
        expression = res        # Update the expression with the result for further calculations
    except Exception as e:
        result.config(text="ERROR")
        expression = ""

# # to clear the result window
def clear_result():
    global expression
    expression = ""
    result.config(text=expression)


# # import required library
from tkinter import *


# # intializing the gui window
calcy=Tk()
calcy.title("Calculator by @Rajput_Riishabh")
calcy.geometry("550x600")
calcy.resizable(False,False)
calcy.config(bg=colb)

# E# create a result label to print the expression and result
result = Label(calcy,width=25,height=2,text= "",font=("arial",30),bg=colb,fg="#fff")
result.pack()
Frame(calcy, width=500, height=2, bg=coldg).pack()


# # Lambda function creates a new function that calls the functions when the button is clicked
# # If you directly pass a function call with arguments (e.g., command=update_result("/")), 
# # the function would be executed immediately during the creation of the button, rather than
# # when the button is clicked.


Button(calcy,text="C", command=lambda: clear_result(), width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg=colr).place(x=3,y=105)
Button(calcy,text="/", command=lambda: update_result("/"), width=5, height=1, font=("arial",30,"bold"), bd=1,fg=colg,bg=coldg).place (x=140,y=105)
Button(calcy,text="%", command=lambda: update_result("%"), width=5, height=1, font=("arial",30,"bold"), bd=1,fg=colg,bg=coldg).place(x=280,y=105)
Button(calcy,text="X", command=lambda: update_result("*"), width=5, height=1, font=("arial",30,"bold"), bd=1,fg=colg,bg=coldg).place(x=420,y=105)

Button(calcy,text="7", command=lambda: update_result("7"), width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg=coldg).place(x=3,y=205)
Button(calcy,text="8", command=lambda: update_result("8"), width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg=coldg).place (x=140,y=205)
Button(calcy,text="9", command=lambda: update_result("9"), width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg=coldg).place(x=280,y=205)
Button(calcy,text="-", command=lambda: update_result("-"), width=5, height=1, font=("arial",30,"bold"), bd=1,fg=colg,bg=coldg).place(x=420,y=205)

Button(calcy,text="4", command=lambda: update_result("4"), width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg=coldg).place(x=3,y=305)
Button(calcy,text="5", command=lambda: update_result("5"), width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg=coldg).place (x=140,y=305)
Button(calcy,text="6", command=lambda: update_result("6"), width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg=coldg).place(x=280,y=305)
Button(calcy,text="+", command=lambda: update_result("+"), width=5, height=1, font=("arial",30,"bold"), bd=1,fg=colg,bg=coldg).place(x=420,y=305)

Button(calcy,text="1", command=lambda: update_result("1"), width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg=coldg).place(x=3,y=405)
Button(calcy,text="2", command=lambda: update_result("2"), width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg=coldg).place (x=140,y=405)
Button(calcy,text="3", command=lambda: update_result("3"), width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg=coldg).place(x=280,y=405)

Button(calcy,text="0", command=lambda: update_result("0"), width=11, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg=coldg).place(x=3,y=505)
Button(calcy,text=".", command=lambda: update_result("."), width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg=coldg).place(x=280,y=505)
Button(calcy,text="=", command=lambda: calculate_result(), width=5, height=3, font=("arial",30,"bold"), bd=1,fg="#fff",bg=colg).place(x=420,y=410)




calcy.mainloop()