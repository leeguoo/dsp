[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>>```python
>> import numpy as np
>> import pylab as plt
>> import random
>> from collections import Counter
>> randnum = np.array([random.random() for i in range(1000)])
>> x, y = zip(*sorted([(k,v) for k,v in Counter(randnum).items()]))
>> x = np.array(x)
>> y = np.array(y)
>> 
>> plt.figure()
>> plt.bar(x,1.0*y/y.sum(),width=1.0/len(x))
>> plt.ylabel("PMF")
>> plt.xlabel("Random Variate")
>> plt.savefig("4_2_pmf.pdf")
>>```
>>![\label{pmf}](4_2_pmf.pdf)
>>\ref{pmf}.
>>```python
>> plt.plot(x,1.0*np.cumsum(y)/y.sum())
>> plt.savefig("4_2_cdf.pdf")
>>```  
