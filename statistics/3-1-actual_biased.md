[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>>```python
>>from collections import Counter
>>import numpy as np
>>import pylab as plt
>>import nsfg
>>
>>resp = nsfg.ReadFemResp()
>>
>>actual = resp.numkdhh.dropna()
>>act_dict = Counter(actual)
>>x = np.array(act_dict.keys())
>>y = np.array(act_dict.values())
>>
>>plt.figure()
>>
>>print "actual mean:", (1.0*x*y/y.sum()).sum()
>>plt.bar(x-0.2,1.0*y/y.sum(),width=0.4,align='center',label='actual')
>>
>>y = x*y
>>print "bias mean:", (1.0*x*y/y.sum()).sum()
>>plt.bar(x+0.2,1.0*y/y.sum(),width=0.4,align='center',label='observed')
>>
>>plt.xlabel("Kid Number")
>>plt.ylabel("PMF")
>>plt.legend()
>>plt.savefig("3_1.png")
>>```
>>actual mean: 1.02420515504
>>bias mean: 2.40367910066
>>![]((https://github.com/leeguoo/dsp/blob/master/statistics/3_1.png)
