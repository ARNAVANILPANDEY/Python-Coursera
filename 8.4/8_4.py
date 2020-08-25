s=input("Enter File Name")
hand=open(s)
lst=[]
for line in hand:
    for word in (line.strip()).split():
        if word in lst:continue
        else:
            lst.append(word)

lst.sort()
print(lst)
