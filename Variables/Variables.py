#Write a program to prompt the user for hours and rate per hour to compute gross pay.


hours_worked = int(input("Please enter your hours "))
hourly_rate = int(input("Please enter your rate "))

gross_pay = hours_worked * hourly_rate

print("Gross pay:", gross_pay)
