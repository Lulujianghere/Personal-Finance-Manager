from datetime import datetime

class FinanceManager:
    def __init__(self):
        self.accounts = {}
        self.transactions = []

    def add_account(self):
        name = input('Enter account name: ')
        if name in self.accounts:
            print(f'Account {name} already exists!')
            return
        try:
            balance = float(input('Enter initial balance: €'))
            self.accounts[name] = balance
            print(f'Account {name}: initial balance €{balance}')
        except ValueError:
            print('Balance must be a number. Please try again.')

    def add_transaction(self):
        account_name = input('Enter account name: ')
        if account_name not in self.accounts:
            print('Account does not exist.')
            return
        try:
            amount = float(input('Enter transaction amount (use negative for expenses): €'))
            if self.accounts[account_name] + amount < 0:
                print('Transaction declined.')
                return
            description = input('Enter description: ')
            date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            self.accounts[account_name] += amount
            self.transactions.append({'account': account_name, 'amount': amount, 'description': description, 'date': date})
            print(f'Transaction done! New balance for {account_name}: €{self.accounts[account_name]}')
        except ValueError:
            print('Amount must be a number. Please try again.')

    def show_accounts(self):
        if not self.accounts:
            print("No accounts found.")
        else:
            print("\n------ Accounts Summary ------")
            sorted_accounts = sorted(self.accounts.items(), key=lambda x: x[0])
            for name, balance in sorted_accounts:
                print(f"{name}: €{balance}")

    def show_transactions(self):
        if not self.transactions:
            print("No transactions found.")
        else:
            print("\n--- Transactions Summary ---")
            for item in self.transactions:
                print(f" {item['date']}: Account: {item['account']}, Amount: €{item['amount']}, Description: {item['description']}")

    def delete_account(self):
        name = input('Enter account name to delete: ')
        if name not in self.accounts:
            print('Account does not exist.')
            return
        check_again = input(f"Enter 'Yes' to confirm deletion of account {name} and all related data: ")
        if check_again.lower() == 'yes':
            self.transactions = [transaction for transaction in self.transactions if transaction['account'] != name]
            del self.accounts[name]
            print(f'Account {name} and related transactions deleted.')
        else:
            print('Account deletion cancelled.')

    def save_data(self):
        with open('finance_data.txt', 'w', encoding='UTF-8') as file:
            file.write('------ Accounts ------\n')
            for account, balance in self.accounts.items():
                file.write(f'{account}: €{balance}\n')

            file.write('\n------ Transactions ------\n')
            for item in self.transactions:
                file.write(f"Account: {item['account']}, Amount: €{item['amount']}, Description: {item['description']}\n")
        print('Data saved to finance_data.txt file.')

    def load_data(self):
        with open('finance_data.txt', 'r', encoding='UTF-8') as file:
            content = file.read()
            print(content)

    def menu(self):
        while True:
            print('-'*3 + ' Personal Finance Manager ' + '-'*3)
            print('1. Add Account')
            print('2. Add Transaction')
            print('3. Show Accounts')
            print('4. Show Transactions')
            print('5. Save Data')
            print('6. Load Data')
            print('7. Delete Account')
            print('8. Exit')
            choice = input('Choose one option (1-8): ')
            if choice == '1':
                self.add_account()
            elif choice == '2':
                self.add_transaction()
            elif choice == '3':
                self.show_accounts()
            elif choice == '4':
                self.show_transactions()
            elif choice == '5':
                self.save_data()
            elif choice == '6':
                self.load_data()
            elif choice == '7':
                self.delete_account()
            elif choice == '8':
                print('Goodbye!')
                break
            else:
                print('Wrong choice. Please try again.')

if __name__ == '__main__':
    manager = FinanceManager()
    manager.menu()





