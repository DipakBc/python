# Calculator using python (first exercise).
'''

// example ans == 1.1 if we use this operator ans will 1.
% modulus 
** example 5**2 == 5*5

'''

def addition(first_num, second_num):
    sum = first_num + second_num
    return sum


def subtraction(first_num, second_num):
    difference = first_num - second_num
    return difference


def multipliction(first_num, second_num):
    product = first_num * second_num
    return product


def division(first_num, second_num):
    divide = first_num / second_num
    return divide

# for user input 
while True:
    operations_options = int(input('''
    Choose operations to perform .
            1  for addition.
            2  for subtraction.
            3  for multiplication.
            4  for division.
    
            Your choice here : '''))

    first_num = int(input("Enter your first number : "))
    second_num = int(input("Enter your second number : "))

    if operations_options == 1:
        print(f"The sum of {first_num} and {second_num} is {addition(first_num, second_num)}.")
        
    elif operations_options == 2:
        print(f"The difference of {first_num} and {second_num} is {subtraction(first_num, second_num)}.")

    elif operations_options == 3:
        print(f"The product of {first_num} and {second_num} is {multipliction(first_num, second_num)}.")

    elif operations_options == 4:
        print(f"The division of {first_num} and {second_num} is {division(first_num, second_num)}")

    else:
        print("Invalid input, try again. Thank You !!!")
        quit()