from matplotlib import pyplot as plt
from collections import Counter

num_friends=[100,49,41,40,25,20,23,34,44,54,222,23,43,12,21,22,33,31,76,67,78,76,98,67,39,29,11]
friend_counts=Counter(num_friends)
xs=range(101)
ys=[friend_counts[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0, 101, 0, 5])
plt.title("Histogram of friends count")
plt.xlabel("#of friends")
plt.ylabel("# of people")
plt.show()




