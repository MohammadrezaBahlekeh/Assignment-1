import colorama
from colorama import Fore
print("BMI Calculator")
W = float(input("enter your Weight (Kg)"))
H = float(input("enter your Height (M)"))

BMI = W/H**2

if BMI <18.5:
    print(Fore.BLUE+" You are Underweight")
elif 18.5<BMI<=24.9:
    print(Fore.GREEN+" You are Normalweight")
elif 25<BMI<=29.9:
    print(Fore.LIGHTYELLOW_EX+" You are Overweight")
elif 30<BMI<=34.9:
    print(Fore.YELLOW+" You are Obesity")
elif 35<BMI<=39.9:
    print(Fore.RED+" You are Extreme Obesity")