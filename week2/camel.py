# Ask user for camel case
camel_case = input("Camelcase: ")

# Convert camel case to snake case
snake_case = " "
for char in camel_case:
    if char.isupper():
        snake_case += "_" + char.lower()
    else:
        snake_case += char

# Remove leading underscore if present
if snake_case.startswith("_"):
    snake_case = snake_case[1:]

# Output the snake case variable name
print("Snake case:", snake_case)