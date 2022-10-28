def add(a, b):
    answer = a + b
    print(f"{str(a)} + {str(b)} = {str(answer)}\n")


def sub(a, b):
    answer = a - b
    print(f"{str(a)} - {str(b)} = {str(answer)}\n")


def mul(a, b):
    answer = a * b
    print(f"{str(a)} * {str(b)} = {str(answer)}\n")


def div(a, b):
    answer = a / b
    print(f"{str(a)} / {str(b)} = {str(answer)}\n")


while True:
    print("A. Addition"
          "\nB. Subtraction"
          "\nC. Multiplication"
          "\nD. Division"
          "\nE. Exit")

    choice = input("Input your choice: ")
    if choice == "A".lower() or choice == "Addition".lower():
        print("Addition")
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        add(num1, num2)
    elif choice == "B".lower() or choice == "Subtraction".lower():
        print("Subtraction")
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        sub(num1, num2)
    elif choice == "C".lower() or choice == "Multiplication".lower():
        print("Multiplication")
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        mul(num1, num2)
    elif choice == "D".lower() or choice == "Division".lower():
        print("Division")
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        div(num1, num2)
    elif choice == "E".lower() or choice == "Exit".lower():
        print("Exiting program...")
        quit()
