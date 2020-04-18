def main():
    numbers = []
    for i in range(5):
        num = int(input("Enter the number: "))
        numbers.append(num)
    print("The largest number is", max(numbers))
    print("The smallest number is", min(numbers))
    print("The first number is", numbers[0])
    print("The last number is", numbers[len(numbers) - 1])
    print("The average is", sum(numbers)/len(numbers))

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    username = input("Enter your name(Case Sensitive): ")
    if username in usernames:
        print("Access Granted.")
    else:
        print("Access denied.")


main()
