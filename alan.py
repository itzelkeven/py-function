thislist = [1, 2, 3]
print(thislist)

def avg(n1,n2,n3):
    return ((n1+n2+n3)/3)

a = avg(thislist[0],thislist[1],thislist[2])
print(a)



def avg2(mylist):
    sum = 0
    for i in mylist:
        sum+=i
    average = sum/len(mylist)
    return average

print(avg2(thislist))
        
