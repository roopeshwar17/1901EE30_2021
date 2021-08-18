print("My name is Jonnakuti Roopeshwar ,Roll no is 1901ee30 ")

def meraki_helper(n):
    
    if(n<10):
        print("YES -",n,"is a meraki number")
        return True
    else:    
     s=str(n)
     l=len(s)
     j=0
     for j in range(0,l-1):
        
        if(abs((int(s[j])-int(s[j+1])))==1):
            continue
        else:
            print("N0 -",n," is not a meraki number")
            return False
    print("Yes -",n, "is a meraki number")
    return True
    

list = [12, 14, 56, 78, 98, 54, 678, 134, 789, 0, 7, 5, 123, 45, 76345, 987654321]
x=0
y=0
for i in list:
    if(meraki_helper(i)):
        x+=1
    else:
        y+=1
print("The input list contains",x,"meraki and",y,"non meraki numbers")
            