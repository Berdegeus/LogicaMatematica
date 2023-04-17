import tkinter as TK
import pyperclip
import io
from tkinter.constants import INSERT
from TruthTable import generateTruthTable
import tkinter.messagebox
import os,sys


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

# create the window
root = TK.Tk( )
root.title("Calculadora de tabela verdade")
root.resizable(0, 0)
root.geometry('680x320')
root.configure(bg='#222226')
 
result = TK.StringVar( )
equation = TK.StringVar( )
result.set(' ')
equation.set(' ')
 
# get the number
def getnum(num):
    temp = equation.get( )
    temp2 = result.get( )
    print(temp)
    print(temp2)
    if temp2 != ' ' :
        temp = ''
        temp2 = ' '
        result.set(temp2)
    temp = temp + num
    equation.set(temp)
    print(equation)
 
# delete the last char
def back( ):
    temp = equation.get( )
    equation.set(temp[:-1])


def parentheses(expression):
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            # Pop all elements until the opening parenthesis
            subexpr = ''
            while stack[-1] != '(':
                subexpr = stack.pop() + subexpr
            stack.pop()  # Remove the opening parenthesis

            # Evaluate the subexpression recursively
            result = evaluate(subexpr)
            stack.append(str(result))
        else:
            stack.append(char)

    # Evaluate any remaining expression in the stack
    while len(stack) > 1:
        left = stack.pop(0)
        op = stack.pop(0)
        right = stack.pop(0)
        result = perform_operation(left, op, right)
        stack.insert(0, str(result))

    return stack[0]

 
# clear the string
def clear( ):
    equation.set(' ')
    result.set(' ')
 
# get the truth table for the string
def run( ):
    temp = equation.get( )
    print(temp)
    buffer = io.StringIO()
    generateTruthTable(temp, reverse=False, markdown=False, file=buffer)
    print(buffer.getvalue())
    result.set(buffer.getvalue())
 
def copy_ans():
    pyperclip.copy(result.get())
    tkinter.messagebox.showinfo("Copiado")

# show the result
show_uresult = TK.Label(root, bg = '#1f1f29', fg = 'white', font = ('Arail', '15'), bd = '0', textvariable = equation, anchor = 'se')
show_dresult = TK.Label(root, bg = '#1f1f29', fg = 'white', font = ('Arail', '10'), bd = '0', textvariable = result, anchor = 'se')
# show_dresult = TK.Text(root,bg='white',fg = 'white',font = ('Arail','10'),bd='0',)
show_uresult.place(x = '10', y = '10', width = '300', height = '50')
show_dresult.place(x = '10', y = '60', width = '300', height = '250')



# Define button dimensions
button_width = 60
button_height = 40

# Define button colors
button_color = '#161617'
button_text_color = 'white'

# Define button font
button_font = ('Arial', 12)
button_font_bold = ('Arial', 12, 'bold')

# Define button spacing
button_padding = 5

# Define button positions
button_positions = {
    'letters': [
        ('A', 405, 10),
        ('B', 465, 10),
        ('C', 525, 10),
        ('D', 405, 90),
        ('E', 465, 90),
        ('F', 525, 90),
        ('G', 585, 90),
        ('H', 405, 170),
        ('I', 465, 170),
        ('J', 525, 170),
    ],
    'operators': [
        ('&', 405, 250),
        ('|', 465, 250),
        ('^', 525, 250),
        ('¬', 585, 170),
    ],
    'others': [
        ('Del', 335, 10),
        ('<->', 335, 90),
        ('->', 335, 170),
        ('Copiar', 335, 250),
        ('MC', 585, 10),
        ('Calc', 585, 250),
        ('(', 10, 10),
        (')', 70, 10),
    ],
}

# Define functions for creating buttons
def create_button(text, x, y, width=button_width, height=button_height, color=button_color,
                  font=button_font, text_color=button_text_color, command=None):
    button = TK.Button(root, text=text, bg=color, fg=text_color, font=font, command=command)
    button.place(x=x, y=y, width=width, height=height)
    return button

def create_letter_buttons():
    for letter, x, y in button_positions['letters']:
        create_button(letter, x, y, command=lambda letter=letter: getnum(letter))

def create_operator_buttons():
    for operator, x, y in button_positions['operators']:
        create_button(operator, x, y,  font=button_font_bold, command=lambda operator=operator: getnum(operator))

def create_other_buttons():
    for text, x, y in button_positions['others']:
        create_button(text, x, y, width=button_width+button_padding*2, height=button_height,
                      color=button_color, font=button_font_bold, text_color=button_text_color,
                      command={
                          'Del': back,
                          '<->': lambda: getnum('<->'),
                          '->': lambda: getnum('->'),
                          'Copiar': copy_ans,
                          'MC': clear,
                          'Calc': run,
                          '(': lambda: getnum('('),
                          ')': lambda: getnum(')'),
                      }[text])

# Create all the buttons
create_letter_buttons()
create_operator_buttons()
create_other_buttons()

root.mainloop()

