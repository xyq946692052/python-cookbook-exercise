prices = {
    'APPLE': 5000,
    'HUAWEI': 4998,
    'VIVO': 3200,
    'XIAOMI': 5999,
    'SANSONG': 2890,
    'OPPO': 4290 
}

min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
sort_price = sorted(zip(prices.values(), prices.keys()))

print('The price of phone: ', prices)
print('min_price: ',min_price, '\nmax_price', max_price)
print('sort of price: ', sort_price)

print('*'*50)

a = {'x':1, 'y':2, 'z':3}
b = {'w':10, 'x':11, 'y':2}
print(a,'\n',b)
#find the same keys
dt = a.keys() & b.keys()
print('a and b has the same key: ',dt)

#find the key in a not in b
dt = a.keys() - b.keys()
print('{} in a not in b'.format(dt))

#find the (key, value) pars in common
dt = a.items() & b.items()
print('a and b has the same (key,value): ',dt)


#if you want to remove the item in dict, do like this
c = {key: a[key] for key in a.keys() - {'z','y'}}
print(c)
