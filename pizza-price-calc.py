# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if size == "S" and add_pepperoni == "Y" and extra_cheese == "Y":
    bill = 18
    print(f"Your final bill is: ${bill}.")
if size == "M" and add_pepperoni == "Y" and extra_cheese == "Y":
    bill = 24
    print(f"Your final bill is: ${bill}.")
if size == "L" and add_pepperoni == "Y" and extra_cheese == "Y":
    bill = 29
    print(f"Your final bill is: ${bill}.")
if size == "S" and add_pepperoni == "Y" and extra_cheese == "N":
    bill = 17
    print(f"Your final bill is: ${bill}.")
if size == "M" and add_pepperoni == "Y" and extra_cheese == "N":
    bill = 23
    print(f"Your final bill is: ${bill}.")
if size == "L" and add_pepperoni == "Y" and extra_cheese == "N":
    bill = 28
    print(f"Your final bill is: ${bill}.")
if size == "S" and add_pepperoni == "N" and extra_cheese == "Y":
    bill = 16
    print(f"Your final bill is: ${bill}.")
if size == "M" and add_pepperoni == "N" and extra_cheese == "Y":
    bill = 21
    print(f"Your final bill is: ${bill}.")
if size == "L" and add_pepperoni == "N" and extra_cheese == "Y":
    bill = 26
    print(f"Your final bill is: ${bill}.")
if size == "S" and add_pepperoni == "N" and extra_cheese == "N":
    bill = 15
    print(f"Your final bill is: ${bill}.")
if size == "M" and add_pepperoni == "N" and extra_cheese == "N":
    bill = 20
    print(f"Your final bill is: ${bill}.")
if size == "L" and add_pepperoni == "N" and extra_cheese == "N":
    bill = 25
    print(f"Your final bill is: ${bill}.")

