def due_amount(total_bill, amount_paid):
    return total_bill - amount_paid

# Input
bill = float(input("Enter total bill amount: "))
paid = float(input("Enter amount paid: "))

# Output
print("Due Amount =", due_amount(bill, paid))