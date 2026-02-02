def get_price(choice):
    if choice == "1":
        return 5, "Single Journey"
    if choice == "2":
        return 10, "Return Ticket"
    if choice == "3":
        return 20, "Day Pass"
    return 0, None


while True:
    print("\n1.Single - ₹5  2.Return - ₹10  3.Day Pass - ₹20  4.Exit")
    choice = input("Choose: ")

    if choice == "4":
        print("Thank you!")
        break

    price, name = get_price(choice)

    if name is None:
        print("Invalid choice!")
        continue

    print("Selected:", name, "₹", price)

    money = int(input("Insert money: ₹"))

    if money >= price:
        print("Ticket issued!")
        if money > price:
            print("Change: ₹", money - price)
    else:
        print("Not enough money!")

# 1.Single - ₹5  2.Return - ₹10  3.Day Pass - ₹20  4.Exit
# Choose: 1
# Selected: Single Journey ₹ 5
# Insert money: ₹10 
# Ticket issued!
# Change: ₹ 5

# 1.Single - ₹5  2.Return - ₹10  3.Day Pass - ₹20  4.Exit
# Choose: 2
# Selected: Return Ticket ₹ 10
# Insert money: ₹20
# Ticket issued!
# Change: ₹ 10

# 1.Single - ₹5  2.Return - ₹10  3.Day Pass - ₹20  4.Exit
# Choose: 3
# Selected: Day Pass ₹ 20
# Insert money: ₹40
# Ticket issued!
# Change: ₹ 20

# 1.Single - ₹5  2.Return - ₹10  3.Day Pass - ₹20  4.Exit
# Choose: 4
# Thank you!