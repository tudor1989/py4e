# rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string. 

try:
  score = float(input("Enter your score here: "))
except:
  pass

def ComputeGrade(score):
  """This function calculates the grade based on the score"""

  if score >= 0.9 and score <= 1.0:
    return "A"
  elif score >= 0.8 and score < 0.9:
    return "B"
  elif score >= 0.7 and score < 0.8:
    return "C"
  elif score >= 0.6 and score < 0.7:
    return "D"
  elif score < 0.6:
    return "F"
  elif score > 1.0:
    return "Bad score"
  else:
    return

# calling the function

ComputeGrade(score)
