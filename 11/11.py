import re
n=0
hand=open('regex_sum_736132.txt')
for line in hand:
    for i in re.findall('[0-9]+',line.rstrip()):
        n=n+int(i)
        #print(i)

print(n)








