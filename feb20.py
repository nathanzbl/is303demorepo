# Toa Pita
# Section 42
# 2/17/2025
# Description: Take input for two numbers.
# Check if the sum of those numbers is the same as their product
from addition import addTwoNumbers
from multiply import multiplyTwoNumbers
x = input(":")
y = input(":")
if(addTwoNumbers(x,y)==multiplyTwoNumbers(x,y)):
    print("The sum and product are the same")
else:
    print("The sum and product are different")