s=input("Enter the name of file")
hand=open(s)
counts=dict()
bc=None
bn=None
for line in hand:
    if(line.startswith('From ')):
        counts[line.split()[1]]=counts.get(line.split()[1],0)+1

for k,v in counts.items():
    if(bc is None or v>bc):
        bc=v
        bn=k

print(bn,bc)
#print(counts)
    


        
