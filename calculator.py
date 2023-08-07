### Function to gather the information for the equation
def equation_input():
    # Prompt the user, and get their starting equation.
    string_equation = input('Enter an equation, with the format XX + YY. I can add, subtract, multiply, and divide.\n')

    # Split their equation string into an array. For the numbers, I also convert the string to int here.
    split_equation = string_equation.split()
    num1 = float(split_equation[0])
    operator = split_equation[1]
    num2 = float(split_equation[2])

    # Call the function to do the math
    do_the_math(num1, num2, operator)

### Function to get rid of the floating 0 in the answer sentence
def remove_zero(number):
    if number % 1 == 0:
        return int(number)
    else:
        return number

### Function to do the operation
def do_the_math(num1, num2, operator):
    match operator:
        case "+":
            final_answer = num1 + num2
        case "-":
            final_answer = num1 - num2
        case "*":
            final_answer = num1 * num2
        case "/":
            final_answer = num1 / num2
        case _:
            print("You have entered an invalid formula. Please try again.")
            return
    
    # Print out the number to the console    
    print("The answer to", remove_zero(num1), operator, remove_zero(num2), "is", remove_zero(final_answer))
        
# Start the program
equation_input()