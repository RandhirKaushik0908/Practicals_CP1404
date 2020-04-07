import random
MIN_SCORE = 0
MAX_SCORE = 100


def main():
    in_file = open('Results.txt', 'w')
    number_of_score = int(input("Enter the number of scores: "))
    while number_of_score < 0:
        number_of_score = int(input("Invalid input! Enter valid score: "))
    for i in range(number_of_score):
        score = random.randint(MIN_SCORE, MAX_SCORE)
        result = calculate_result(score)
        print("{} is {}".format(score, result), file=in_file)
    in_file.close()


def calculate_result(score):
    if score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


main()
