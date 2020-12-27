# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ≤ 1000, is the number of solutions maximised?
import time # This program takes about 16 seconds to run on my Lenovo Thinkpad -- Matthew Bruno 12/27/2020
import statistics
from statistics import mode
start = time.time()

a_b_c = []
perimeter = []

upper_limit = 1000

def pythag_triple(limit):
    for a in range(1, int(limit/2)):
        for b in range(1, int(limit/2)):
            for c in range(1, int(limit/2)):
                if a*a + b*b == c*c and a + b + c <= limit and a < b < c:
                    a_b_c.append([a,b,c])
                    perimeter.append(a+b+c)

pythag_triple(upper_limit)

answer = mode(perimeter)
print(answer)

stop = time.time()
print("Time: ", stop - start)