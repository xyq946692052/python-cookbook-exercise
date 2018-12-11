from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

# get the frequency of occurrence of three word 
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)


# get the quantity of word
print(word_counts['not'])
print(word_counts['eyes'])


# add the quantity of count
data = ['why','are','you','not','looking','in','my','eyes', 'in']
for k in data:
    word_counts[k] += 1

print(word_counts['eyes'])


word_counts.update(data)
print(word_counts)    

a = Counter(words)
b = Counter(data)
c = a + b
print(c)

d = a - b
print(b)


