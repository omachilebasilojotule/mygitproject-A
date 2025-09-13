#python week 1 assignment
op= input("Enter your operator +, -, *,/")
print("Enter your operator:")
num1 = int(input("ENTER THE FIRST NUMBER"))
num2 = int(input("ENTER THE SECOND NUMBER"))
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("invalid operator")
