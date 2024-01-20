import tkinter as tk
from tkinter import ttk
from datetime import datetime

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title('Expense Tracker')

        # Expense input fields
        self.label_amount = ttk.Label(root, text='Amount:')
        self.label_amount.grid(row=0, column=0, padx=10, pady=10)
        self.entry_amount = ttk.Entry(root, width=20)  # Increased width
        self.entry_amount.grid(row=0, column=1, padx=10, pady=10)

        self.label_category = ttk.Label(root, text='Category:')
        self.label_category.grid(row=1, column=0, padx=10, pady=10)
        self.entry_category = ttk.Entry(root, width=20)  # Increased width
        self.entry_category.grid(row=1, column=1, padx=10, pady=10)

        # Button to add expense
        self.add_button = ttk.Button(root, text='Add Expense', command=self.add_expense, width=30)  # Increased width
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Expense listbox
        self.expense_listbox = tk.Listbox(root, height=15, width=50)  # Increased height and width
        self.expense_listbox.grid(row=3, column=0, columnspan=2, pady=10)

        # Load initial expenses from a file
        self.load_expenses()

    def add_expense(self):
        amount = self.entry_amount.get()
        category = self.entry_category.get()

        if amount and category:
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

            expense_info = f"{timestamp} - Amount: {amount}, Category: {category}"
            self.expense_listbox.insert(tk.END, expense_info)

            # Save the expense to a file
            with open('expenses.txt', 'a') as file:
                file.write(expense_info + '\n')

            # Clear input fields
            self.entry_amount.delete(0, tk.END)
            self.entry_category.delete(0, tk.END)

    def load_expenses(self):
        # Load expenses from the file and populate the listbox
        try:
            with open('expenses.txt', 'r') as file:
                expenses = file.readlines()
                for expense in expenses:
                    self.expense_listbox.insert(tk.END, expense.strip())
        except FileNotFoundError:
            # Handle the case when the file is not found
            pass

def main():
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()

if __name__ == "__main__":
    main()
