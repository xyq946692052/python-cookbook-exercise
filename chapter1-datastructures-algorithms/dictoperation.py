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
