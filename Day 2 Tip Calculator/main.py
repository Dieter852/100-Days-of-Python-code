print("Welcome to the tip calculator!")

bill_total = float(input("How much was the total bill?\nR"))
tip = int(input("How much tip would you like to give? 10, 12 or 15?\n"))
people_paying = int(input("How many people will split the bill?\n"))

total = ((tip / 100) * bill_total) + (bill_total / people_paying)

print(f"Each person should pay: R{total:.2f}")