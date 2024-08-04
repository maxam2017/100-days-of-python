print("Welcome to the tip calculator!")

# ask total bill
total_bill = float(input("What was the total bill? $"))

# ask tips (%)
tips = int(input("How much tip would you like to give? 10, 12, or 15? "))

# ask how many people
people = int(input("How many people to split the bill? "))

bill_with_tips = total_bill * (1 + tips / 100)
bill_per_person = bill_with_tips / people
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${final_amount}")