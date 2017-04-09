[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>>```python
>>import thinkstats2
>>import nsfg
>>import numpy as np
>>
>>def CohenD(x1,x2):
>>    return (x1.mean()-x2.mean())/np.sqrt((len(x1)*x1.var()+len(x2)*x2.var())/(len(x1)+len(x2)))
>>
>>preg = nsfg.ReadFemPreg()
>>live = preg[preg.outcome == 1]
>>
>>w1 = live[live.birthord==1]["totalwgt_lb"].dropna()
>>w2 = live[live.birthord!=1]["totalwgt_lb"].dropna()
>>print CohenD(w1,w2)
>>```
>> -0.088672363332
