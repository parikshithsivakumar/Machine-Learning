mylist=[2,7,4,1,3,6]
count=0
for i in range(len(mylist)):
    for j in range(i+1,len(mylist)):
        if mylist[i]+mylist[j]==10:
           count=count+1
           print("[",mylist[i],mylist[j] ,"]")
print(count)
