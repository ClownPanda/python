def sum_list(lst):
    result=sum(lst)
    print("The sum of list is",result)

def mul_list(lst):
    n=len(lst)
    mul=1
    for i in range (0,n):
        mul=lst[i] * mul
    print("The multiplication of all elements of the list is",mul)

def max_min_numbers(lst):
    print("The largest number in list is",max(lst))
    print("The smallest number in list is",min(lst))

def remove_dup(lst):
    dic=dict.fromkeys(lst)
    result=list(lst)
    print("The list without duplicates is",result)

lst = [3,5,2,6,2,9,4]
print("The original list is",lst)

sum_list(lst)
mul_list(lst)
max_min_numbers(lst)
remove_dup(lst)

