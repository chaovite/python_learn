import numpy as np
from matplotlib import pyplot as plots
# generate random number according to geometric distribution
num_samples = 1000
p           = 1./2
samples     = np.random.geometric(p, size=num_samples)
rewards     = np.power(2.0,samples)

#count rewards to plot histogram
unique,cnts = np.unique(rewards, return_counts=True)

print("%s : %10.5f" % ('Mean reward:', rewards.mean()))

# plot the distribution of rewards.
plots.figure(1)
plots.hist(rewards, bins = 100)
plots.figure(2)
plots.stem(unique, cnts, linefmt='b-',markerfmt='bo')
plots.xlim([0, 500])
plots.show()

