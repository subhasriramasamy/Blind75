n = int(input("Enter the value of n: "))
prev,curr = 1,1
for i in range(1,n):
    next = prev+curr
    prev = curr
    curr = next

print(curr)