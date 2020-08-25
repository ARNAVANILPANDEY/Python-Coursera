s=input("Enter file name")
try:
    hand=open(s)
except:
    print("wrong name")
    quit()
    
for line in hand:
    line=line.upper()
    print(line.rstrip())
