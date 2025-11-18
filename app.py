# Daily Study Tracker Program
print("Welcome to my study tracker!")
# Ask for input
hours = input("How many hours did you study today? ")
#Error handling
try:
  hours = float(hours)
except ValueError:
  print("Please enter a valid number. ")
  exit()
# Calculation
weekly = hours * 7
# Output
print(f"If you study like this every day, you'll study about {weekly} hours this week.")
