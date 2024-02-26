while True:
    num = input("Enter first number or 'exit' to quite':")
    if num.lower()=="exit":
        print("Exiting the Screen")
        break
    op = input("Enter Operator(*,/,+,-) :")
    num2 = int(input("Enter second number:"))
    
    num1 = int(num)
    if op == '+':
        print(num1+num2)
    
    elif op == '-':
        print(num1-num2)
    elif op == '/':
        print(num1/num2)
    elif op == '*':
        print(num1*num2)
    else:
        print("Invalid Operator")

