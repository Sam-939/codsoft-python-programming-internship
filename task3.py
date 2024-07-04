import random
upper_letters = ['A','B','C','D','E','F','G','H','I','J','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lower_letters = ['a','b','c','d','e','f','g','h','i','j','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','(',')','*','~']
print("password Generator!")
length = int(input("Enter the length of password: "))
user_input = input("For specifications enter(yes/no): ")
password_list=[]
password = ''
if user_input == 'yes':
    no_upletters = int(input("Enter the number of upper letters: "))
    no_lowletters = int(input("Enter the number of lower letters: "))
    no_symbols = int(input("Enter the number of symbols: "))
    no_numbers = int(input("Enter the number of numbers: "))
    if length != no_upletters+no_lowletters+no_symbols+no_numbers:
        print("Your specifications are not matched. \n Please enter your specifications that match the length of your password." )
    else:
        for i in range(0,no_upletters):
            char1=random.choice(upper_letters)
            password_list.append(char1)
        for i in range(0,no_lowletters):
            char2=random.choice(lower_letters)
            password_list.append(char2)
        for i in range(0,no_symbols):
            char3=random.choice(symbols)
            password_list.append(char3)
        for i in range(0,no_numbers):
            char4=random.choice(numbers)
            password_list.append(char4)
        random.shuffle(password_list)
        for i in password_list:
            password += i
        print("Your generated password is :",password)
else:
    for i in range(0,length):
        all=upper_letters+lower_letters+numbers+symbols
        char = random.choice(all)
        password += char
    print("Your generated password is:",password)
    