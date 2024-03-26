num1, operator, num2 = input("Enter calculations: ").split()
num1, num2 = int(num1), int(num2)
if operator == "+":
    print(f"{num1} + {num2} = {num1+num2}")
elif operator == "-":
    print(f"{num1} - {num2} = {num1-num2}")
elif operator == "*":
    print(f"{num1} * {num2} = {num1*num2}")
elif operator == "/":
    print(f"{num1} / {num2} = {num1/num2}")
else:
    print("Sorry use either + - * and / next time")
