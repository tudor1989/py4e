# write a program to propt for a score between 0.0 and 1.0.
# If the score is out of range, print an error message.
# If the score is between 0.0 and 1.0, print a grade using the following table;

#  Score     Grade
#>= 0.9        A
#>= 0.8        B
#>= 0.7        C
#>= 0.6        D
# < 0.6        F


try:
  grade = float(input("Enter a score: "))

except ValueError:
  print("Bad score")

if round(grade,2) >= 0.9:
  print("A")

elif round(grade,2) >= 0.8:
  print("B")

elif round(grade,2) >= 0.7:
  print("C")

elif round(grade,2) >= 0.6:
  print("D")

elif round(grade,2) < 0.6:
  print("F")
