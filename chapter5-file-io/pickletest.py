import pickle

f = open('somedata', 'wb')

pickle.dump([1, 2, 3, 4], f)
pickle.dump('hello', f)
pickle.dump({'Apple', 'Bannaner', 'Pear'}, f)
f.close()

f = open('somedata', 'rb')
print(pickle.load(f))
print(pickle.load(f))
print(pickle.load(f))
f.close()

with open('somedata', 'rb') as f:
    print(pickle.load(f))
