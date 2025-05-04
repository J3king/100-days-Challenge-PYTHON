#Mini Calculator 
#It has Restart option after an operation end 
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
  if not x.is_integer() or x < 0:
      return "Error! Factorial only works with non-negative integers."
  x = int(x)
  if x == 0 or x == 1:
      return 1
  result = 1
  for i in range(2, x + 1):
      result *= i
  return result

while True:
  print("\nSelect operation:")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("5. Square")
  print("6. Cube")
  print("7. Square Root")
  print("8. Factorial")
  print("9. Exit")

  choice = input("Enter choice (1-9): ").strip()

  if choice == '9':
      print("Exiting the calculator.")
      break

  try:
      num1 = float(input("Enter first number: "))
  except ValueError:
      print("Invalid input! Please enter a number.")
      continue

  if choice in ['1', '2', '3', '4']:
      try:
          num2 = float(input("Enter second number: "))
      except ValueError:
          print("Invalid input! Please enter a number.")
          continue

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
  else:
      print("Invalid input!")

  restart = input("Do you want to Restart? (yes/no): ").strip().lower()
  if restart != 'yes':
      print("Thank you for using the calculator.")
      break
