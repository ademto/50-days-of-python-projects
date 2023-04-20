from calculator import add, sub, mul, div

print("Welcome to the calculator app!\n")

first_number = float(input("Please enter the first number: "))
second_number = float(input("Please enter the second number: "))

print("\nPlease select an operation: \n1. Add \n2. Subtract \n3. Multiply \n4. Divide")

choice = input("\nEnter your choice (1/2/3/4): ")

if choice == "1":
    result = add(first_number, second_number)
elif choice == "2":
    result = sub(first_number, second_number)
elif choice == "3":
    result = mul(first_number, second_number)
elif choice == "4":
    result = div(first_number, second_number)
else:
    print("Invalid choice")

print("The result is:", result)
