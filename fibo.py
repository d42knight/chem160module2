# Write your code here :-)
prev2 = 0
prev1 = 1
for i in range(20):
    current = prev2 + prev1
    print(current)
    prev2 , prev1 = prev1 , current
