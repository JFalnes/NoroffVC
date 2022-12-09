import tkinter as Tk
from tkinter import messagebox
import sv_ttk
def addition():
    num_one = input_one.get()
    num_two = input_two.get()
    
    tk_sum = int(num_one) + int(num_two)

    message = f'Sum: {tk_sum}'
    result_label.config(text=message)


def subtraction():
    num_one = input_one.get()
    num_two = input_two.get()
    
    tk_sum = int(num_one) - int(num_two)
    
    message = f'Sum: {tk_sum}'
    result_label.config(text=message)

     


app = Tk.Tk()
app.title('GUI Calculator')
app.resizable(False, False)
app.geometry(('600x400'))
sv_ttk.set_theme("dark")



result_label = Tk.Label(app, text='Sum: ')
result_label.grid(row=9, column=2)

first_label = Tk.Label(app, text='First Input')
first_label.grid(row=3, column=2)

second_label = Tk.Label(app, text='Second Input')
second_label.grid(row=6, column=2)

input_one = Tk.Entry(app, width=40)
input_one.grid(row=5, column=2)

input_two = Tk.Entry(app, width=40)
input_two.grid(row=7, column=2)

sub_button= Tk.Button(app, text='-', command=subtraction)
sub_button.grid(row=8, column=1)

add_button = Tk.Button(app, text='+', command=addition)
add_button.grid(row=8, column=2)

app.mainloop()