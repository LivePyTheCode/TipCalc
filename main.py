print("Welcome to the tip calculator!")
bill = int(input("What was the total bill?: \n"))

tip = float(input("What percentage tip would you like to give?: \n"))

split = int(input("How many people are splitting the bill: \n"))

total_split = round(((bill * tip + bill) / split), 2)

print(total_split)
