# Get number of terms from the user
n = int(input("Enter the number of terms: "))

# First two terms
a, b = 0, 1
fibonacci = []

if n <= 0:
    print("Please enter a positive number.")
elif n == 1:
    fibonacci.append(a)
else:
    fibonacci.append(a)
    fibonacci.append(b)
    for _ in range(2, n):
        next_term = a + b
        fibonacci.append(next_term)
        a, b = b, next_term

# Print the sequence
print("Fibonacci sequence:")
print(fibonacci)
