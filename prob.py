#import needed modules
import collections
import scipy.stats as stats
import numpy as np 
import matplotlib.pyplot as plt

#example 1 frequency
testlist = [1, 4, 5, 6, 9, 9, 9]

c = collections.Counter(testlist)

print "Here is the first example..." + "\n"
print c

# calculate the number of instances in the list
count_sum = sum(c.values())

for k,v in c.iteritems():
  print "The frequency of number " + str(k) + " is " + str(float(v) / count_sum) + "\n"

#example 1 box plot
print "Let's save this data in a box plot..."
x = [1, 4, 5, 6, 9, 9, 9]
plt.boxplot(x)
#plt.show()
plt.savefig("6digitsboxplot.png")
print "SAVED."

#example 1 histogram
print "\n" + "Let's save this data in a histogram..." 
#x = [1, 4, 5, 6, 9, 9, 9]
plt.hist(x, histtype='bar')
#plt.show()
plt.savefig("6digitshistogram.png")
print "SAVED."

#example 2 frequency
testlist = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

c = collections.Counter(testlist)

print "\n" + "Here is the second example..."
print c

# calculate the number of instances in the list
count_sum = sum(c.values())

for k,v in c.iteritems():
  print "The frequency of number " + str(k) + " is " + str(float(v) / count_sum) + "\n"


#example 2 box plot
print "Let's save this data in a box plot..."
x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
plt.boxplot(x)
plt.savefig("1thru9boxplot.png")
print "SAVED."

#example 2 histogram
print "\n" + "Let's save this data in a histogram..." 
#x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
plt.hist(x, histtype='bar')
plt.savefig("1thru9histogram.png")
print "SAVED."

#qq-plots
print "\n" + "Let's save a random, normal distribution on a qq-plot..."
plt.figure()
test_data = np.random.normal(size=1000)   
graph1 = stats.probplot(test_data, dist="norm", plot=plt)
plt.savefig("NormRndqq-plot.png")
print "SAVED."
print "\n" + "Let's graph a random, uniform distribution on a qq-plot..."
plt.figure()
test_data2 = np.random.uniform(size=1000)   
graph2 = stats.probplot(test_data2, dist="norm", plot=plt)
plt.savefig("UniformRndqq-plot.png")
print "SAVED."