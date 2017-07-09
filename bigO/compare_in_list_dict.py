# This program compare the time complexity of the in: operator
# on python list and dictionary.

import matplotlib.pyplot as plt
import timeit
import random
time_dict = []
time_list = []
n_list    = list(range(10000, 1000001,50000))
print("%10s, %10s, %10s" % ('size','list time','dict time'))
for i in n_list:
    index = random.randrange(i)
    x = list(range(i))
    t = timeit.Timer("index in x", "from __main__ import x, index")
    lst_time  = t.timeit(number=1000)
    y = {j:0 for j in range(i)}
    t = timeit.Timer("index in y", "from __main__ import y, index")
    d_time    = t.timeit(number=1000)
    print("%10d, %10.3f, %10.3f"%(i, lst_time, d_time))
    time_dict.append(d_time)
    time_list.append(lst_time)

# make plots
plt.plot(n_list, time_list,'bo')
plt.plot(n_list, time_dict,'ro')
plt.xlabel("Size")
plt.ylabel("Time")
plt.legend(["list","dict"])
plt.show()
