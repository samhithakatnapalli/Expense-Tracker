from art import logo

expenses = []

def add_expenses():
    amount = int(input("Enter the amount you want to add: ₹"))
    description = input("Enter the expense description: ")
    category = input("Enter the expense category: ")
    expenses.append({
        "amount": amount,
        "description": description,
        "category": category,
    })

def view_expenses():
    if expenses:
        for expense in expenses:
            print(f"You spent ₹{expense["amount"]} on {expense['description']}")
    else:
        print("No expenses added")

def view_total_spent():
    total = 0
    for expense in expenses:
        total += expense['amount']
    print(f"Total spent: {total}")

def view_expenses_by_category():
    money_spent = 0
    category_to_view = input("What category would you like to view? ")
    for expense in expenses:
        if expense['category'] == category_to_view:
            money_spent += expense['amount']
            print(f"You spent ₹{expense["amount"]} on {expense['description']}.\nTotal spent: {money_spent}")
        else:
            print("No expenses were added under this category.")


while True:
    print(logo)

    print("1 : Add Expenses\n2 : View all Expenses\n3 : View total spent\n4 : View by Category\n5 : Exit")
    try:
        choose = int(input("Choose an option (1-5): "))
    except ValueError:
        print("Invalid option")
        choose = int(input("Choose an option (1-5): "))
        continue

    if choose not in range(1,6):
        print("Invalid option")
        continue

    if choose == 1:
        add_expenses()
    elif choose == 2:
        view_expenses()
    elif choose == 3:
        view_total_spent()
    elif choose == 4:
        view_expenses_by_category()
    elif choose == 5:
        print("Thank you for using this program!")
        break


