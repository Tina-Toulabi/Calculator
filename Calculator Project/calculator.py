def calculator():
    print("Simple Python Calculator")
    operations = {
        '1': ('Add', lambda x, y: x + y),
        '2': ('Subtract', lambda x, y: x - y),
        '3': ('Multiply', lambda x, y: x * y),
        '4': ('Divide', lambda x, y: x / y if y != 0 else "Error: Division by zero")
    }

    while True:
        print("\nOptions:")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")
        print("5. Exit")

        choice = input("Choose an operation (1-5): ")
        if choice == '5':
            break
        if choice not in operations:
            print("Invalid choice.")
            continue

        try:
            a = float(input("First number: "))
            b = float(input("Second number: "))
            result = operations[choice][1](a, b)
            print("Result:", result)
        except ValueError:
            print("Please enter valid numbers.")

calculator()

