# Prompt the user, and get their starting equation.
string_equation = input('Enter an equation, with the format XX + YY. I can add, subtract, multiply, and divide.\n')

# Split their equation string into an array. For the numbers, I also convert the string to int here.
split_equation = string_equation.split()
num1 = int(split_equation[0])
operator = split_equation[1]
num2 = int(split_equation[2])

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
    print(string_equation, " = ", final_answer)
            
# Call the math function to do the thing.
do_the_math(num1, num2, operator)