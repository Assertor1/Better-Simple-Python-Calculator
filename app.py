def calc():
    ''' This is a functiion which when called, perform calculation tasks which user wants '''

    num1 = float(input("Enter first number: "))
    op = input("Enter operator: ")
    num2 = float(input("Enter second number: "))

    if op == "+" :
        print(num1 + num2)
    elif op == "-" :
        print(num1 - num2)
    elif op == "/" :
        print(num1 / num2)
    elif op == "*" :
        print(num1 * num2)
    elif op == "**" :
        print(num1 ** num2)
    else:
        print("Invalid operator")

while True:
    i = int(input("Press 1 to Continue, otherwise press 0\n")) 
    if i == 1:
        calc()
    else:
        break

