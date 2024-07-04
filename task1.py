print("welecome to the calcuLator")
while True:
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))
    print("Please enter the operation you want to perform: \n 1 for addition \n 2 for subtraction \n 3 for multiplication \n 4 for division ")
    operation = input("Enter your operation: ")
    if operation in ('1','2','3','4'):
        #perform operation
        if operation == "1":
            print(f"The Addition of {n1} and {n2} is",n1+n2)
        elif operation == '2':
            print(f"The Difference of {n1} and {n2} is",n1-n2)
        elif operation == '3':
            print(f"The Multiplication of {n1} and {n2} is",n1*n2)
        elif operation == '4':
            if n2 != 0:
                print(f"The Division of {n1} and {n2} is",n1/n2)
            else:
                print("Division by zero is not performed.\n Invalid operation.\n Please try again")
    op = input("Do you want to continue? (yes/no): ")
    if op.lower() == 'yes':
        continue
    else:
        print('Goodbye!')
        break


        