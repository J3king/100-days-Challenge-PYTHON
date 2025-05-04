# Countdown Timer
# This script implements a simple countdown timer in Python.
import time

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02}:{secs:02}"
        print(timer, end="\r")  # overwrite the line
        time.sleep(1)
        seconds -= 
    print("Time's up! 🎉")

# Example usage:
try:
    total_seconds = int(input("Enter time in seconds: "))
    countdown(total_seconds)
except ValueError:
    print("Please enter a valid number.")
