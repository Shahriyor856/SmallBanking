

def show_balance(balance):

    print("***********************")
    print(f"The current balance is ${balance:.2f}")
    print("***********************")


def deposit():
    amount = float(
        input("Enter the amount:"))
    print("***********************")
    if amount <= 0:
        print("***********************")
        print("You cannot deposit a negative amount or zero.")
        print("***********************")
        return 0
    else:
        return amount


def withdraw(balance):
    print("***********************")
    amount = float(
        input("Enter the amount:"))
    print("***********************")

    if amount > balance:
        print("***********************")
        print("You do not have enough funds.")
        print("***********************")
        return 0

    elif amount <= 0:
        print("***********************")
        print("Amount must be greater than 0.")
        print("***********************")
        return 0
    else:
        return amount


def history(transactions):
    print("***********************")
    print("Transaction History:")
    print("***********************")

    if not transactions:

        print("No transactions yet.")

    else:
        for i, (kind, amount) in enumerate(transactions, 1):
            print(f"{i}. {kind}: ${amount:.2f}")
    print("***********************")


def main():

    balance = 0
    transaction_history = []
    is_running = True

    while is_running:
        print("***********************")
        print("    Banking Program    ")
        print("***********************")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Transaction History")
        print("5.Exit")
        print("***********************")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            amount = deposit()
            if amount > 0:
                balance += amount
                transaction_history.append(("Deposited", amount))
        elif choice == "3":
            amount = withdraw(balance)
            if amount > 0:

                balance -= amount
                transaction_history.append(("Withdrew", amount))
        elif choice == "4":
            history(transaction_history)
        elif choice == "5":
            is_running = False
            print(
                "You have exited the banking program.")
        else:
            print("***********************")
            print(
                "That is not a valid choice.")
            print("***********************")

    print("***********************")
    print("Thank you, have a nice day!")
    print("***********************")


if __name__ == "__main__":
    main()
