"""
Given two numbers x and y as input, find the HCF of x and y. Note that HCF is the largest number that will divide both x and y. If we run a loop from 1 to the smaller of x and y, we can find the largest number that divides both x and y.
Input-> x=20, y=50
Output-> 10
"""

x = 20
y = 50
hcf = 0
if (x>y):
  smaller = y
else:
  smaller = x
for i in range(1,smaller+1):
  if(x%i==0 and y%i==0):
   hcf = i
print(hcf)
