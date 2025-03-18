def calculator():
    print("Welcome to the my Calculator!")
 
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    
  
    print("\nChoose the operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    operation = input("Enter the operation symbol (+, -, *, /): ").strip()
    

    if operation == '+':
        result = num1 + num2
        print(f"\nResult: {num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"\nResult: {num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"\nResult: {num1} * {num2} = {result}")
    elif operation == '/':
        if num2 == 0:
            print("\nError: Division by zero is undefined.")
        else:
            result = num1 / num2
            print(f"\nResult: {num1} / {num2} = {result}")
    else:
        print("\nInvalid operation. Please select one of +, -, *, /.")
calculator()
