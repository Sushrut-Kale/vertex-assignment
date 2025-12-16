print("1. Addition" )
print("2. Subtraction" )
print("3. Multiplication")
print("4. Division" )
print("5. Exit")

choice = int(input("Enter your choice (1-5): "))

if choice == 1:
	a = float(input("Enter first number: "))
	b = float(input("Enter second number: "))
	print ("Result:", a + b)
elif choice == 2:
	a = float(input("Enter first number: "))
	b = float(input("Enter second number: "))
	print ("Result:", a - b)
elif choice == 3:
	a = float(input("Enter first number: "))
	b = float (input("Enter second number: "))
	print ("Result:", a * b)
elif choice == 4:
	a = float(input("Enter first number: "))
	b = float(input("Enter second number: "))
	if b != 0:
		print ("Result:", a / b)
	else:
		print("Error: Cannot divide by zero")
elif choice == 5:
	print("Exiting...")

else:
	print("Invalid choice")