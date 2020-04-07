"""
Use string formatting to produce the output:
(Notice where the values go and also the float formatting / number of decimal places.)
1922 Gibson L-5 CES for about $16,035!
Using a for loop with the range function and string formatting (do not use a list), produce the following output (right-aligned numbers):
  0
 50
100
150"""

name = "Gibson L-5 CES"
year = 1922
cost = 16035.4
print("{} {} for ${:,.2f}".format(year, name, cost))

for number in range(4):
    print("{:3}".format(50 * number))