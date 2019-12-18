from random import choices
ntrials=1000000
limit=1000
count=0
for i in range(ntrials):
    rand=choices(range(1,limit+1),k=3)
    if rand[0]+rand[1]<=rand[2]:
        count=count+1
print("Fraction=",count/ntrials)
