hand=open("mbox-short.txt")
d=dict()
for line in hand:
    if line.startswith("From "):
        pos=line.find(":")
        k=(line[pos-2:]).split(":")[0]
        d[k]=d.get(k,0)+1



for k,v in sorted(d.items()):print(k,v)
