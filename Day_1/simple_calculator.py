"""
Making of a Simple calculator
Owner: @MusabPirzada
"""

num_1 = int(input("Enter 1st Number: "))
num_2 = int(input("Enter 2nd Number: "))

operation = input("Enter Operator (+,-,/,*,^): ")
if operation == '+':
    print(num_1 + num_2)
elif operation == '-':
    print(num_1 - num_2)
elif operation == '*':
    print(num_1 * num_2)
elif operation == '/':
    print(num_1 / num_2)
elif operation == '^':
    print(num_1 ** num_2)
