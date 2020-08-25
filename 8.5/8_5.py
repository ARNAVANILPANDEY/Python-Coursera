s=input("Enter file name")
hand=open(s)
c=0
for line in hand:
    if line.startswith('From:'):
        c=c+1
        print(line.split()[1])

print('There were',c,'lines in the file with From as the first word')
