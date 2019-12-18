from random import choice
dim = 2
trials = 1000
steps = 10000
gothome = 0

for i in range(trials):
    point = [0]*dim
    for step in range(steps):
        for j in range(dim):
            point[j] += choice((-1,1))
        if point.count(0) == dim:
            gothome += 1
            break
        
print("Fraction that got home = %f in %d dims" % (gothome/trials,dim))
