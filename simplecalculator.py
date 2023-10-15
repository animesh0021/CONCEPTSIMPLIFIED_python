def calc():
    while True:
        print("Enter '1' to add two numbers")
        print("Enter '2' to subtract two numbers")
        print("Enter '3' to multiply two numbers")
        print("Enter '4' to divide two numbers")
        print("Enter 'any natural no. greater than 4' to end the program")
    
        user_input = input(": ")

        if user_input >="5":
            break
        elif user_input in ["1", "2", "3", "4"]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if user_input == "1":
                c = a + b
                print(a, "+", b, "=", c)
                print("Answer : ",c)

            elif user_input == "2":
                c = a - b
                print(a, "-", b, "=", c)
                print("Answer : ",c)

            elif user_input == "3":
                c = a * b
                print(a, "*", b, "=", c)
                print("Answer : ",c)
                
            elif user_input == "4":
                c = a / b
                print(a, "/", b, "=", c)
                print("Answer : ",c)
        else:
            print("Invalid Input")
calc()