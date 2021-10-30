
while True:
    print("\n\n\n")
    print("\t\t|------------------------------------------------------")
    num1 = float(input("\t\t|Enter first number: "))
    choice = input("\t\t|Enter Operation: ")
    num2 = float(input("\t\t|Enter second number: "))

    if choice in ('+', '-', '*', '/'):
        if choice == '+':
            print("\t\t|Ans  :   ",num1+num2)
            print("\t\t|------------------------------------------------------")

        elif choice == '-':
            print("\t\t|Ans  :   ",num1-num2)
            print("\t\t|------------------------------------------------------")

        elif choice == '*':
            print("\t\t|Ans  :   ",num1*num2)
            print("\t\t|------------------------------------------------------")

        elif choice == '/':
            print("\t\t|Ans  :   ",num1/num2)
            print("\t\t|------------------------------------------------------")
        break
    else:
        print("\t\t|Ans  :   Syntex Eror")
        print("\t\t|------------------------------------------------------")
