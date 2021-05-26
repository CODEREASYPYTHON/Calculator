while True:
    number_one = input("Enter the first number:")
    query = input("Which arithmetic operation should be carried out? (+,-,/.,*):")
    number_two = input("Enter the second number:")

    Equal_1 = float(number_one)
    Equal_2 = float(number_two)

    if query == "+":
        print("Your result",Equal_1+Equal_2)
    if query == "-":
        print("Your result",Equal_1-Equal_2)
    if query == "*":
        print("Your result",Equal_1*Equal_2)
    if query == "**":
        print("Your result",Equal_1**Equal_2)
    if query == "/":
        print("Your result",Equal_1/Equal_2)
    if query == "//":
        print("Your result",Equal_1//Equal_2)