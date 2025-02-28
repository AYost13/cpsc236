taxRate = .06

def sales_tax(total):
    global taxRate
    return round(total * taxRate, 2)

def full_total(total, taxAmount):
    return round(total + taxAmount, 2)