# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both lists and tuples are sequences of elements. The difference is that a list is mutable, while a tuple is immutable. Tuples can work as keys in dictionaries, because of their immutability.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Both lists and sets are collections of elements. Sets are unordered collections of unique elements, while lists are ordered collections of elements (duplicates are allowed).  
>>```python
>>#example of using list
>>a = []
>>a.append(1)
>>```
>>```python
>>#example of using sets
>>#remove duplicates of a list
>> a = range(10)+range(5)
>> a = list(set(a))
>>```
>>It is faster to find an element in a set, because sets are implemented using hash tables. The speed of element finding does not depend on the sizes of sets. On the other hand, to find an element in list, the whole list needs to be searched.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Python's `lambda` is a operator. It is used to creat anonymous functions.  
>>```python
>>#example
>>a = [('rice', 50), ('sugar', 40), ('salt', 100), ('peper', 30)]
>>sorted(a,key=lambda a: a[1])
>>```

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehension is a way to create a list from an iterable (e.g. another list).
>>```python
>>#create a list using list comprehension
>>a = [x*2 for x in range(10)]
>>#create the same list using map
>>a = map(lambda x: x*2, range(10))
>>#create the same list using filter
>>a = filter(lambda x: x%2==0, range(20))
>>#set comprehension
>>{x*2 for x in range(10)}
>>#dictionary comprehension
>>{x:x*2 for x in range(10)}
>>```

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  
```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937  

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850  

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





