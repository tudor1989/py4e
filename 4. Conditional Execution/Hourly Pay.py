# Hourly Pay

# calculate Hourly pay including overtime cases 

hours = int(input("Enter number of hours worked: "))
rate = int(input("Enter rate per hour: "))

pay_regular = 40 * float(rate)


if hours > 40: 
  print("Overtime")
  hours_overtime = hours - 40
  rate_overtime = float(rate) + float(rate) * 0.5 
  pay_overtime_bonus = hours_overtime * rate_overtime
  pay = pay_regular + pay_overtime_bonus
  print(pay, pay_overtime_bonus)
else:
  print("Regular", pay_regular)
