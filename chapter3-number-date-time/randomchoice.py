import random
values = [1, 2, 3, 4, 5 ,6 ,7 ,8, 9, 0]

# random generate one num in values
for i in range(5):
    print(random.choice(values)) 

# random generate one array
for i in range(5):
    print(random.sample(values,2))
    print(random.sample(values,3))

# disrupt the order of array
for i in range(5):
    random.shuffle(values)
    print(values)

# generate the int number
for i in range(5):
    print(random.randint(0,10))

# generate the random float
for i in range(5):
    print(random.random())

# generate the number random
print(random.getrandbits(200))

random.seed(10)
print(random.random())
random.seed(b'bytedata')
print(random.random())
