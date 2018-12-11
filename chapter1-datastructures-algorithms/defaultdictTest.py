from collections import defaultdict

# the item insert into container with order, include the repeat data
dl = defaultdict(list)
dl['a'].append(1)
dl['b'].append(2)
dl['a'].append(3)
dl['c'].append(4)
dl['b'].append(5)
dl['a'].append(6)
dl['b'].append(2)
print('defaultdict(list): ',dl)

#the item insert into container not need order, not repeat data
ds = defaultdict(set)
ds['a'].add(1)
ds['b'].add(2)
ds['a'].add(1)
ds['a'].add(2)
ds['b'].add(3)
ds['a'].add(4)
print('defaultdict(set): ',ds)



