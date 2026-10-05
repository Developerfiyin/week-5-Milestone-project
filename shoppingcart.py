

items = []
prices = []

print("===================================")
print("  WELCOME  TO  SHOPPING STORE")
print("===================================")

while True:
    print("\nMENU")
    print("1. Add an item")
    print("2. View cart")
    print("3. Remove an item")
    print("4. View total")
    print("5. Quit")

    choice = input("Choose an option: ")

    # Add an item
    if choice == "1":
        item = input("What would you like to add? ")
        price = float(input("How much does it cost? $"))

        items.append(item)
        prices.append(price)

        print(item, "has been added to your cart! ")

    # View the cart
    elif choice == "2":
        if len(items) == 0:
            print("\nYour cart is currently empty.")
        else:
            print("\n========== YOUR CART ==========")

            for index in range(len(items)):
                print(f"{index + 1}. {items[index]} - ${prices[index]:.2f}")

            print("===============================")

    # Remove an item
    elif choice == "3":
        if len(items) == 0:
            print("\nThere is nothing to remove because your cart is empty.")
        else:
            print("\n========== REMOVE ITEM ==========")

            for index in range(len(items)):
                print(f"{index + 1}. {items[index]} - ${prices[index]:.2f}")

            remove_item = int(input("Enter the item number you want to remove: "))

            # Check that the number is valid
            if remove_item >= 1 and remove_item <= len(items):

                # Convert 1-based index to 0-based index
                index = remove_item - 1

                removed_item = items[index]

                items.pop(index)
                prices.pop(index)

                print(removed_item, "has been removed from your cart. ")

            else:
                print("That item number is not valid.")

    # View total
    elif choice == "4":
        total = 0

        for price in prices:
            total += price

        print(f"\nYour current total is: ${total:.2f}")

    # Quit
    elif choice == "5":
        total = 0

        for price in prices:
            total += price

        print("\n===================================")
        print("        THANK YOU FOR SHOPPING!")
        print("===================================")
        print(f"Your final total is: ${total:.2f}")
        print("Come back soon! ")
        break

    # Invalid menu option
    else:
        print("Please choose an option from 1 to 5.")

