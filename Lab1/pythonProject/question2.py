print("Enter the number of list elements")
n = int(input())
mylist = []
if n < 3:
  print("Range determination not valid")
else:
 for i in range(n):
    print("Enter the element")
    mylist.append(int(input()))
 print(mylist)
 mylist.sort()
 print(mylist)
 max=max(mylist)
 min=min(mylist)
 range=max-min
 print("Range is",range)