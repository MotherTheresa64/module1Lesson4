#Discount calculator portion

#Variables for grocery items/list and their prices
milk = 5
eggs = 3
coffee = 10

#Calculating total price
total_cost = milk + eggs + coffee

#Applying discount (10% off)
discount_name = total_cost * 0.90

#Printing out total price and discounted price
print("Total price: $" + str(total_cost))
print("Discounted price: $" + str(discount_name))


#     <--Final exercise below this line-->

# Function to add two numbers
def add (num1, num2):
    return num1 + num2
# Function to subtract two numbers
def subtract (num1, num2):
    return num1 - num2
# Function to multiply two numbers
def multiply (num1, num2):
    return num1 * num2
# Function to divide two numbers    
def divide (num1, num2):
    return num1 / num2
  
# Display the available operations
print("Select operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Take input from the user
operation = input("Enter operation (1/2/3/4): ")

# Take input from the user for the two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operation == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif operation == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif operation == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif operation == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid input")