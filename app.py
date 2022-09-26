name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts=dict()
for line in handle:
    line=line.rstrip()
    if not line.startswith('From:'):continue
    line=line.split()
    for x in line:
        if x not in counts:
            counts[x]=1
        else:
            counts[x]+=1
email=None
ave=None
for word,count in counts.items():
    if email is None or count > ave:
        email=x
        ave=count
        print(email,counts[email])
