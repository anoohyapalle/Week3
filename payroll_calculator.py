number_of_hours = int(input("Number of hours worked by the employee: "))
hourly_rate = int(input("Amount paid per hour: "))
def calculate_pay(hours, rate):
    pay = hours * rate
    return pay
total_pay = calculate_pay(number_of_hours, hourly_rate)
print("The total pay for the employee is: Rs.", total_pay)
