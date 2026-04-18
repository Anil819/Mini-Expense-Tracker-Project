import datetime

expenses = []

print("====== Welcome To Expense Tracker ========")

while True:
    print("\n===== MENU =====")
    print("1. Add Expense")
    print("2. View All Expense")
    print("3. View Total Expenses")
    print("4. Exit\n")

    choice = int(input("Enter your Choice (1-4): "))

    # ADD EXPENSE
    if choice == 1:
        date = input(f"{datetime.datetime.now()}")
        category = input("Enter category (Food, Travel, etc): ")
        description = input("Enter description : ")
        amount = float(input("Enter Amount : "))

        expense = {
            "date": date,
            "category": category,
            "amount": amount,
            "description": description,
        }

        expenses.append(expense)

        # Save to file
        with open("Expenses.txt", "a") as file:
            file.write(
                f"{datetime.datetime.now()} -> {date}, {category}, {description}, {amount}\n"
            )

        print(" Expense added successfully")

    # VIEW ALL EXPENSES
    elif choice == 2:
        if len(expenses) == 0:
            print(" No expense recorded")
        else:
            print("\n Your Expenses:")
            count = 1

            with open("Viewexpense.txt", "a") as file:
                for kharcha in expenses:
                    output = f"{count} -> {kharcha['date']}, {kharcha['category']}, {kharcha['description']}, {kharcha['amount']}"
                    print(output)

                    # append to file
                    file.write(f"{datetime.datetime.now()} -> {output}\n")

                    count += 1

    # TOTAL EXPENSE
    elif choice == 3:
        if len(expenses) == 0:
            print(" No expense recorded")
        else:
            total = 0
            for kharcha in expenses:
                total = total + kharcha["amount"]

            print(f"\n Total Expense = {total}")

            # append total to file
            with open("Totalexpense.txt", "a") as file:
                file.write(f"{datetime.datetime.now()} -> Total Expense = {total}\n")
            total = total + 1
    # EXIT
    elif choice == 4:
        print(" Thank you! Visit Again")
        break

    else:
        print(" Invalid Input, Try Again")
