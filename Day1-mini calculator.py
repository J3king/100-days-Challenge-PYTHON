def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Can't divide by zero."
    else:
        return x / y

def square(x):
    return x * x

def cube(x):
    return x * x * x

def square_root(x):
    if x < 0:
        return "Error! Can't take square root of negative number."
    else:
        return x ** 0.5
    
def factorial(x):
    if x < 0:
        return "Error! Can't take factorial of negative number."
    elif x == 0 or x == 1:
        return 1
    else:
        result = 1
        for i in range(2, x + 1):
            result *= i
        return result

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Square")
print("6. Cube")
print("7. Square Root")
print("8. Factorial")
print("9. Exit")

choice = input("Enter choice (1/2/3/4/5/6/7/8/9): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", subtract(num1, num2))
elif choice == '3':
    print("Result:", multiply(num1, num2))
elif choice == '4':
    print("Result:", divide(num1, num2))
elif choice == '5':
    print("Result:", square(num1))
elif choice == '6':
    print("Result:", cube(num1))
elif choice == '7':
    print("Result:", square_root(num1))
elif choice == '8':
    print("Result:", factorial(num1))
elif choice == '9':
    print("Exiting the calculator.")
else:
    print("Invalid input!")