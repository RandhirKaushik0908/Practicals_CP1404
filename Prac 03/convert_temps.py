import random
TEMP_LIMIT = 200


def main():
    get_input()
    input_file = open('temps_input.txt', 'r')
    output_file = open('temps_output.txt', 'w')
    for value in input_file:
        fahrenheit = float(value)
        celsius = convert_to_celsius(fahrenheit)
        print("{}".format(celsius), file=output_file)
    input_file.close()
    output_file.close()


def get_input():
    input_file = open('temps_input.txt', 'w')
    float_number = int(input("Enter the number of float values: "))
    while float_number < 0:
        float_number = int(input("Invalid Input! Enter the number of float values: "))
    for i in range(float_number):
        temp_value = random.uniform(-TEMP_LIMIT, TEMP_LIMIT)
        print("{}".format(temp_value), file=input_file)
    input_file.close()


def convert_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()
