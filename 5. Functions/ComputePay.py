# rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters(hours and rate)

# prompt the user for hours and rate variables

hours = int(input("Enter number of hours worked: "))
rate = int(input("Enter rate per hour: "))


def ComputePay(hours, rate):
  """Function to calculate regular pay and overtime bonus"""
  pay_regular = 40 * float(rate)


  if hours > 40: 
    
    hours_overtime = hours - 40
    rate_overtime = float(rate) + float(rate) * 0.5 
    pay_overtime_bonus = hours_overtime * rate_overtime
    pay_overtime = pay_regular + pay_overtime_bonus
    
    return f"Pay with overtime bonus {pay_overtime}"

  else:
    return f"Regular pay {pay_regular}"


# call function

ComputePay(hours, rate)
