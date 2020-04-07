try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        denominator = int(input("Denominator cannot be zero. Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")

# 1. ValueError occurs when the numerators or denominators is not a whole number.
# 2. ZeroDivisionError occurs when the denominator is zero.
