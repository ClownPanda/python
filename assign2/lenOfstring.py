def way_1(stri):
    n=len(stri)
    print("The length of",stri,"is",n)

def way_2(stri):
    c=0
    for i in stri:
        c=c+1
    print("The length of",stri,"is",c)

def way_3(stri):
    c = 0
    while stri[c:]:
        c += 1
    print("The length of",stri,"is",c)

def way_4(stri):
    result = sum( 1 for i in stri)
    print("The length of",stri,"is",result)
    
    


stri=input("Enter the string: ")    

way_1(stri)
way_2(stri)
way_3(stri)
way_4(stri)