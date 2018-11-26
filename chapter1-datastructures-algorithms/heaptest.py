import heapq

nums = [1,3,6,8,2,4,-1,7,0,12,55,8,21,66]
print(heapq.nlargest(3, nums))    #get three the first three numbers in nums
print(heapq.nsmallest(3, nums), end='\n')   #get three the smallest number in nums

print('*'*50)

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.0},
    {'name': 'AAPL', 'shares': 50, 'price': 431.1},
    {'name': 'MBQ', 'shares': 100, 'price': 61.5},
    {'name': 'YHOO', 'shares': 100, 'price': 11.0},
    {'name': 'ACME', 'shares': 100, 'price': 781.66},
]

#compare with price
cheap = heapq.nsmallest(3, portfolio, lambda s:s['price'])
expensive = heapq.nlargest(3, portfolio, lambda s:s['price'])
print('cheap:{},\nexpensive: {}\n'.format(cheap, expensive))

print('*'*50)

#sort with heapq
heap = list(nums)
heapq.heapify(heap)
print('Before: {} \nAfter:{}'.format(nums,heap))
print('Get the smallest item: ',heap[0])

