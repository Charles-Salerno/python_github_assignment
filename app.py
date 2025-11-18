print("Welcome to my study tracker!")

hours = input("How many hours did you study today? ")

try:
  hours = float(hours)
except ValueError:
  print("Please enter a valid number. ")
  exit()

weekly = hours * 7

print(f"If you study like this every day, you'll study about {weekly} hours this week.")
