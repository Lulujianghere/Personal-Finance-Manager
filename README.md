# Personal Finance Manager

A simple Python tool to manage personal finances, allowing users to add accounts, track transactions, and view financial summaries. Data is saved and loaded from a file for future use.

## Features

- Add and manage accounts.
- Track income and expenses.
- View balances and transaction history.
- Save and load data from a file.
- Delete accounts and transactions.

## Installation
Clone the repository:

   ```bash
   git clone https://github.com/Lulujianghere/Personal-Finance-Manager.git
   ```

## Example Usage

1. **Adding an Account**:
   - When you run the program and choose the option to add an account, you will be prompted to enter the account name and an initial balance. Example input:
   
     ```bash
     Enter account name: Savings
     Enter initial balance: €500
     ```

2. **Adding a Transaction**:
   - To track income or expenses, select the option to add a transaction. Example input:
   
     ```bash
     Enter account name: Savings
     Enter transaction amount (use negative for expenses): €-100
     Enter description: Grocery shopping
     ```

3. **Viewing Accounts and Transactions**:
   - After adding accounts and transactions, you can view the balances and transaction history by selecting the "Show Accounts" and "Show Transactions" options. Example output:
   
     ```bash
     --- Accounts Summary ---
     Savings: €400

     --- Transactions Summary ---
     28/11/2024 12:34:56: Account: Savings, Amount: €-100, Description: Grocery shopping
     ```

4. **Saving Data**:
   - Save your data to a file by selecting the "Save Data" option. This will create or update a file called `finance_data.txt` with the current account and transaction details.

