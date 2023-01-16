"""Write a program that asks the user for two numbers. Then ask them if they would like to add, subtract, divide, or multiply these numbers. Perform the chosen operation on the values, showing the operation being performed.​"""

def addition(input1,input2):
  res = input1+input2
  print(res)
def substraction(input1,input2):
  if(input1>input2):
      res = input1-input2
  else:
      res = input2-input1
  
  print(res)
def multiplication(input1,input2):
  res = input1*input2
  print(res)
def division(input1,input2):
  try:
    res = input1/input2
  except ZeroDivisionError as e:
      print(e)
  else:
      print(res)

def inputtaken():
  input1 = int(input('Enter input1 as integer:'))
  input2 = int(input('Enter input2 as integer:'))
  

  inputoperation =  input('Enter input operation as (+,-,*,/)')

  if(inputoperation=='+'):
    addition(input1,input2)
  elif(inputoperation=='-'):
    substraction(input1,input2)
  elif(inputoperation=='*'):
    multiplication(input1,input2)
  elif(inputoperation=='/'):
    division(input1,input2)
  

inputtaken()
