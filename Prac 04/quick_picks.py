from random import randint


def main():
    num_of_picks = int(input("Enter the number of quick picks: "))
    while num_of_picks < 0:
        num_of_picks = int(input("Invalid Input! Enter the number of quick picks: "))
    for i in range(num_of_picks):
        quick_pick = []
        for j in range(6):
            random_num = randint(1, 45)
            while random_num in quick_pick:
                random_num = randint(1, 45)
            quick_pick.append(random_num)
        quick_pick.sort()
        result = (" ".join("{:2}".format(num) for num in quick_pick))
        print(result)


main()
