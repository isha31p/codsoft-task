while True:
    
    num1 = float(input("Enter first num: "))
    num2 = float(input("Enter second num: "))

    print("\nSelect operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    choice = input("\nEnter operation (1/2/3/4): ")

    if choice == '1':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif choice == '2':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif choice == '3':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error! Division by zero.")
    else:
        print("Invalid input! Please select a valid operation.")
    
    continue_choice = input("\nDo you want to continue calculating? (yes/no): ").lower()
    if continue_choice != 'yes':
        print("Exiting the calculator. Goodbye!")
        break


