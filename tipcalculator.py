def calculate_total_bill(bill:float, tip:float)->float:
    tip_amount = (tip/100) * bill
    final_bill = bill + tip_amount
    return final_bill

bill = float(input("Enter the bill amount: "))
tip = float(input("Enter tip % "))
print(calculate_total_bill(bill, tip))