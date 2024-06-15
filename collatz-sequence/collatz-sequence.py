"""
My implementation of Collatz Sequenze
"""

import sys
import time

print("Collatz Sequence, or the 3n + 1 problem.")
print("""
      The collatz sequence is a sequence of numbers prduced from a starting number n:
      (1) If n is even, the next number n is n / 2
      (2) If n is odd, the next number n is n * 3 + 1
      (3) If n is 1, stop, or else repeat
      """)

print("Enter a starting number greater than 0, or (q)uit")
response = input("> ")

if not response.isdecimal() or response == "0":
    print("You must enter an integer greater than 0, exiting...")
    sys.exit()

n = int(response)
# end means nothing should be appended to the output
# flush means the output is immediately displayed without being buffered
print(n, end="", flush=True)

while n != 1:
    if n % 2 == 0:
        n = n // 2  # Floor division
    else:
        n = 3 * n + 1

    print(", " + str(n), end="", flush=True)
    time.sleep(0.1)

print()
