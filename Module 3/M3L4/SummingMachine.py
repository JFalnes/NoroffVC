"""Create a script called SummingMachine.py. 
In the script, create a function called summing_machine. 
The function should receive no argument. 
It should continuously ask the user to enter a number until they enter a value to stop, 
e.g. 's'. The values entered must be added together, and the final result returned to the calling code. 
Demonstrate the use of the function in the main section of your script."""

def summing_machine():
    value = []
    while True:
        user_input = input('Input: ')
        if user_input != 's':
            value.append(int(user_input))
        else:
            return sum(value)

a = summing_machine()
print(a[0])