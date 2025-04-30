"""This project:
- Make an account 
- Add balance 
- Withdraw amount
- Deposit amount"""

class Account:
    def __init__(self, name, age, balance=0):
        self.name = name
        self.age = age
        self.balance =  balance
    
    def AccountInfo(self):
        return f"Name: {self.name}\nAge: {self.age}\nBalace: {self.balance}"
    
    def withdraw(self, subtract):
        self.balance=self.balance-subtract
        return self.balance
    def deposit(self, add):
        self.balance=self.balance+add
        return self.balance

def main():
    while True:
        print("1. Make account")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")
        choice = int(input("Enter a number: "))
        if choice == 1:
            while True:
                name = input("Enter your name: ").strip()
                if not name:
                    print("You didn't enter anything.")
                elif not name.replace(" ", "").isalpha():
                    print("Please enter a valid name!")
                else:
                    break

            while True: 
                try:
                    age = int(input("Enter your age: "))
                    break
                except ValueError:
                    print("Enter a valid age!")

            while True:
                try:
                    balance = int(input("Enter your balance: "))
                    break
                except ValueError:
                    print("Enter a valid number!")
            ac = Account(name, age, balance)
            print(ac.AccountInfo())
        elif choice == 2:
            while True:
                try:
                    subtract = int(input("Enter withdraw amount: "))
                    break
                except ValueError:
                    print("Enter a valid number!")
            print("Total balance is:", ac.withdraw(subtract))
        elif choice == 3:
            while True:
                try:
                    add = int(input("Enter deposit amount: "))
                    break
                except:
                    print("Enter a valid number!")
            print("Total balance is:", ac.deposit(add))
        elif choice == 4:
            break


if __name__ == "__main__":
    main()