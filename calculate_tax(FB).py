"""
Write a program to calculate tax if Salary and Tax Brackets are given as list in the form
[ [10000, .3],[20000, .2], [30000, .1], [None, .1]]. 
You don’t know in the beginning how many tax brackets are there. You have to test for all of them
"""
def calculate_tax(levels,salary):
    prev = 0
    left = salary
    tax = 0
    i = 0
    while left > 0:
        level = levels[i]
        tax_percentage = level[1]
        salary_range = level[0]
        if not level[0]:
            return tax + left * tax_percentage
        taxable_salary_range = min(salary_range - prev,left)
        tax += tax_percentage * taxable_salary_range
        left = left - taxable_salary_range
        prev = level[0]
        i+=1

    return tax

print(calculate_tax([[10000, .1],[20000, .2], [30000, .3], [None, .4]],45000))
print(calculate_tax([[10000, .1],[20000, .2], [30000, .3], [None, .4]],25000))