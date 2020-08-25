s=input("Enter file name")
hand=open(s)
c=0
q=0
for line in hand:
    if (line.startswith('X-DSPAM-Confidence:')):
        c=c+1
        q=q+float(line[line.find(' '):].strip())

print("Average spam confdence:",(q/c))
