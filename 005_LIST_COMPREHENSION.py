import time

###FOR LOOP
start = time.time()
cube_numbers = []
for n in range(0,20000000):
    if n % 2 == 1:
        cube_numbers.append(n**3)
end = time.time()
print("Computation time LOOP %f secs" % (end - start)) #Computation time 5.938188 secs

start = time.time()
cube_numbers = [n**3 for n in range(0,20000000) if n%2==1]
end = time.time()
print("Computation time LIST COM %f secs" % (end - start))