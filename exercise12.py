taxable_income = int(input("Enter you income here:$ "))
if taxable_income <= 10000:
    tax_payable = 0
    print(f"Tax income to pay is: {tax_payable}")
elif 10000 < taxable_income <= 20000:
    tax_payable = (taxable_income - 10000) * 10/100
    print(f"Tax income to pay is: {tax_payable}")
else:
    tax_payable = 10000 * 10/100 + (taxable_income - 20000) * 20/100
    print(f"Tax income to pay is: {tax_payable}")






































