"""
What did you see on line 1? What was the smallest number you could have seen, what was the largest?

What did you see on line 2? What was the smallest number you could have seen, what was the largest?Could line 2 have produced a 4?

What did you see on line 3? What was the smallest number you could have seen, what was the largest?

Write code, not a comment, to produce a random number between 1 and 100 inclusive.

"""

import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# 12 Smallest number = 5, Largest = 20
# 7 Smallest number = 3, Largest = 9, No, as only poss numbers are 3,5,7,9.
# 5.230219838465269, Smallest number = 2.5, Largest = 5.5

print(random.randint(1, 100))
