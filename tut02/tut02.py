print("My name is Roopeshwar, roll no:1901EE30")
def isdigit(a):
    list=[]
    var=1
    for i in range(len(a)):
        if(type(a[i])!=int):
            list.append(a[i])
            var=0
    if(var==0):
        print('please enter a valid input list. Invalid inputs detected:',list)
        exit()
    else:
        return

def get_memory_score(n):
    memory=[]
    score=0
    for i in n:
        if i in memory:
            score+=1
        else:
            if(len(memory)<5):
                memory.append(i)
            elif(len(memory)==5):
                memory.append(i)
                memory.remove(memory[0])
    return score

input_nums = [3,4,5,3,2,1]
isdigit(input_nums)
var=get_memory_score(input_nums)
print("score:",var)

