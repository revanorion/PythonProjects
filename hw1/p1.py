import locale
locale.setlocale(locale.LC_ALL, '')
hours_worked = float(input("Enter the number of hours worked this week: "))
rate_per_hour = float(input("Enter the salary rate per hour (do not include the '$' sign): "))
overage, overtime, overtime_hour, overtime_rate = 0.0, 0.0, 40.0, 1.5
bonus = float(input("Enter bonus: ")) if input("Did the worker get a bonus ? (y/n) ") == 'y' else 0.0
if hours_worked > overtime_hour:
    overage = (hours_worked - overtime_hour)
    overtime = overage * rate_per_hour * overtime_rate
total_salary = (hours_worked - overage) * rate_per_hour + overtime + bonus
print("The total salary is ", locale.currency(total_salary, grouping=True),
      " (overtime pay ", locale.currency(overtime, grouping=True), ")")
