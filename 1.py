import math

print("Calculator")
print("+")
print("-")
print("/")
print("*")
print("Sin")
print("Cos")
print("Tan")
print("Cot")
print("Sqrt")
print("Fac")

Operator = input("Please enter the oprator that you want")

if Operator == "+" or Operator == "*" or Operator == "-" or Operator == "/":
    Firstnumber = float(input("Please enter your first number : "))
    Secondnumber = float(input("Please enter your second number : "))
elif Operator == "sin" or Operator == "cos" or Operator == "tan" or Operator == "cot":
    Firstnumber = float(input("Please enter your number : "))

if Operator == "+":
     Result = Firstnumber + Secondnumber
     print(Result)

elif Operator == "*":
     Result = Firstnumber * Secondnumber
     print(Result)

elif Operator == "-":
     Result = Firstnumber - Secondnumber
     print(Result)

elif Operator == "/":
     if Secondnumber>0:
          Result = Firstnumber / Secondnumber
          print(Result) 
     else:
          print("ERROR")    

elif Operator == "sin":
     Result = math.sin(math.radians(Firstnumber))
     print(Result)

elif Operator == "cos":
     Result = math.cos(math.radians(Firstnumber))
     print(Result)

elif Operator == "tan":
     Result= math.tan(math.radians(Firstnumber))
     print(Result)

elif Operator == "cot":
     Result = 1 / math.tan(math.radians(Firstnumber)) 
     print(Result)

elif Operator == "sqrt":
     if Firstnumber>0:
          Result = math.sqrt(Firstnumber)
          print(Result)
     else:
          print("ERROR")

elif Operator == "fac":
     Result= math.factorial(Firstnumber)
     print(Result)


