expression = input("Enter an arithmetic expression (x y z): ")

x, operator, z = expression.split()
x = int(x)
z = int(z)

result = None

if operator == "+":
    result = x + z
elif operator == "-":
    result = x - z
elif operator == "*":
    result = x * z
elif operator == "/":
    result = x / z

if result is not None:
    print(f"The result is: {result:.1f}")
else:
    print("Invalid arithmetic expression.")