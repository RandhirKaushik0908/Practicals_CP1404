# 1
user_name = input("Please enter your name: ")
out_file = open('Name.txt', 'w')
print(user_name, file=out_file)
out_file.close()

# 2
file = open('Name.txt', 'r')
print("Your name is", file.read().strip())

# 3
num_file = open('numbers.txt', 'r')
num1 = int(num_file.readline())
num2 = int(num_file.readline())
total = num1 + num2
print("The sum of first two numbers is", total)
num_file.close()


# 4
num_file = open('numbers.txt', 'r')
total = 0
for line in num_file:
    number = int(line)
    total += number
print("The sum total of numbers is", total)
num_file.close()
