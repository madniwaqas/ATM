import tkinter as tk
from tkinter import messagebox

class ATM:
    def __init__(self, balance=0):
        self.balance = balance
        self.pin = None

    def set_pin(self, new_pin):
        if len(new_pin) == 4 and new_pin.isdigit():
            self.pin = new_pin
            return True
        return False

    def verify_pin(self, entered_pin):
        return entered_pin == self.pin if self.pin is not None else False

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:  # Combined condition
            self.balance -= amount
            return True
        return False

class ATM_GUI:
    def __init__(self, master, atm):
        self.master = master
        master.title("ATM")
        self.atm = atm
        self.create_widgets()

    def create_widgets(self):
        # ... (GUI elements as before)

        self.pin_label = tk.Label(self.master, text="PIN:")
        self.pin_label.grid(row=0, column=0, padx=5, pady=5)
        self.pin_entry = tk.Entry(self.master, show="*")
        self.pin_entry.grid(row=0, column=1, padx=5, pady=5)

        self.set_pin_button = tk.Button(self.master, text="Set/Verify PIN", command=self.set_or_verify_pin)
        self.set_pin_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.balance_button = tk.Button(self.master, text="Check Balance", command=self.check_balance)
        self.balance_button.grid(row=2, column=0, columnspan=2, pady=5)

        self.deposit_label = tk.Label(self.master, text="Deposit Amount:")
        self.deposit_label.grid(row=3, column=0, padx=5, pady=5)
        self.deposit_entry = tk.Entry(self.master)
        self.deposit_entry.grid(row=3, column=1, padx=5, pady=5)
        self.deposit_button = tk.Button(self.master, text="Deposit", command=self.deposit)
        self.deposit_button.grid(row=4, column=0, columnspan=2, pady=5)

        self.withdraw_label = tk.Label(self.master, text="Withdraw Amount:")
        self.withdraw_label.grid(row=5, column=0, padx=5, pady=5)
        self.withdraw_entry = tk.Entry(self.master)
        self.withdraw_entry.grid(row=5, column=1, padx=5, pady=5)
        self.withdraw_button = tk.Button(self.master, text="Withdraw", command=self.withdraw)
        self.withdraw_button.grid(row=6, column=0, columnspan=2, pady=5)

        self.result_label = tk.Label(self.master, text="")
        self.result_label.grid(row=7, column=0, columnspan=2, pady=10)

    def set_or_verify_pin(self):
        entered_pin = self.pin_entry.get()
        if self.atm.pin is None:
            if self.atm.set_pin(entered_pin):
                messagebox.showinfo("Success", "PIN set successfully!")
            else:
                messagebox.showerror("Error", "Invalid PIN. Please enter a 4-digit number.")
        elif self.atm.verify_pin(entered_pin):  # Simplified verification
            messagebox.showinfo("Success", "PIN verified successfully!")
        else:
            messagebox.showerror("Error", "Incorrect PIN.")
        self.pin_entry.delete(0, tk.END)

    def check_balance(self):
        entered_pin = self.pin_entry.get()
        if self.atm.verify_pin(entered_pin):
            balance = self.atm.check_balance()
            self.result_label.config(text=f"Your balance is: ${balance}")
        else:
            messagebox.showerror("Error", "Incorrect PIN or PIN not set.") #Combined message
        self.pin_entry.delete(0, tk.END)

    def deposit(self):
        entered_pin = self.pin_entry.get()
        if self.atm.verify_pin(entered_pin):
            try:
                amount = float(self.deposit_entry.get())
                if self.atm.deposit(amount):
                    self.result_label.config(text="Deposit successful.")
                else:
                    messagebox.showerror("Error", "Invalid deposit amount.")
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please enter a number.")
        else:
            messagebox.showerror("Error", "Incorrect PIN or PIN not set.")
        self.deposit_entry.delete(0, tk.END)
        self.pin_entry.delete(0, tk.END)

    def withdraw(self):
        entered_pin = self.pin_entry.get()
        if self.atm.verify_pin(entered_pin):
            try:
                amount = float(self.withdraw_entry.get())
                if self.atm.withdraw(amount):
                    self.result_label.config(text="Withdrawal successful.")
                else:
                    messagebox.showerror("Error", "Insufficient funds or invalid amount.")
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please enter a number.")
        else:
            messagebox.showerror("Error", "Incorrect PIN or PIN not set.")
        self.withdraw_entry.delete(0, tk.END)
        self.pin_entry.delete(0, tk.END)


root = tk.Tk()
atm = ATM()
gui = ATM_GUI(root, atm)
root.mainloop()