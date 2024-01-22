lst = [3,5,2,6,2,9,4]
n=len(lst)
mul=1
for i in range (0,n):
    mul=lst[i] * mul
print("The multiplication of all elements of the list is",mul)