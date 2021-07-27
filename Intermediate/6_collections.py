# collections: Counter, nametuple, defaultdict, deque, OrderedDict

from collections import Counter, namedtuple, defaultdict, deque, OrderedDict

a = "aaaabbbccc"

mycounter = Counter(a)
print(mycounter.items())
print(mycounter.keys())
print(mycounter.values())
print(mycounter.most_common(1)) # specifiy the number of most common, specify the index to get key or value
print(list(mycounter.elements())) # get all the elements