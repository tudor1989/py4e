def main():
    
  num_list = []
  while True:

    num = input("Enter a value: ")

    if num == 'done':
      break
    
    try:
      int(num) == True
    
    except ValueError:
      print("Please enter a number!")
    
    else:
      num_list.append(int(num))


  #print(num_list)


  sum = 0
  count = 0
  avg = 0

  for elem in num_list:
    sum += elem
    count += 1

  print("Sum of elements is: ", sum)
  print("Count of elements is: ", count)
  print("Avg of elements is: ", (sum/count))
