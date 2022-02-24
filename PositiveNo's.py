l1=[]
n=int(input("Enter size of list : "))
for i in range(0,n):
    values=int(input("Enter element of list: "))
    l1.append(values)
print("List :",l1)   
print("Positive numbers are: ")
for i in l1:
    if i >= 0:
       print(i)
