import random, math
inside = 0
ntrials = 100000
for i in range(ntrials):
    x = random.random()
    y = random.random()
    if (x*x+y*y)<1.0:
        inside += 1
pi = 4.*inside/ntrials
print("N=%d Error=%8.5f "%(ntrials, pi - math.pi))
