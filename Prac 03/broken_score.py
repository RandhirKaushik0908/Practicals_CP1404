"""
Broken program to determine score status

"""
import random
MIN_SCORE = 0
MAX_SCORE = 100


def main():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    result = calculate_result(score)
    print(result)
    random_score = random.randint(MIN_SCORE, MAX_SCORE)
    random_result = calculate_result(random_score)
    print("Random number: {} is {}.".format(random_score, random_result))


def calculate_result(score):
    if score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


main()
