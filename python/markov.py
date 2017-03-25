#!/usr/bin/python

# Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

# ```bash
# ./markov.py chains.txt 40
# ```

# A possible output would be:

# > show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

# There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.

import random
import sys

class MarkovTxt(object):
    def __init__(self,fname):
        f = open('chains.txt','r')
        lines = f.readlines()
        f.close()
        txt = ''
        for line in lines:
            txt += line[:-1]
            txt += " "
        self.words = txt.split()
        self.order_1_get_dict()
        self.order_2_get_dict()

    def order_2_get_dict(self):
        words = self.words
        digrams_dict = {}
        for i in range(len(words)-2):
            k = (words[i],words[i+1])
            if digrams_dict.get(k,None):
                digrams_dict[k].append(words[i+2])
            else:
                digrams_dict[k] = [words[i+2]]
        self.digrams_dict = digrams_dict

    def order_2_output(self,n):
        digrams_dict = self.digrams_dict
        k = random.choice(digrams_dict.keys())
        output_list = list(k)
        for i in range(n):
            v = random.choice(digrams_dict[k])
            output_list.append(v)
            k = (k[1],v)
        return " ".join(output_list)

    def order_1_get_dict(self):
        words = self.words
        grams_dict = {}
        for i in range(len(words)-1):
            k = words[i]
            if grams_dict.get(k,None):
                grams_dict[k].append(words[i+1])
            else:
                grams_dict[k] = [words[i+1]]
        self.grams_dict = grams_dict

    def order_1_output(self,n):
        grams_dict = self.grams_dict
        k = random.choice(grams_dict.keys())
        output_list = [k]
        for i in range(n):
            v = random.choice(grams_dict[k])
            output_list.append(v)
            k = v
        return " ".join(output_list)

fname, n = sys.argv[1:]
n = int(n)

MT = MarkovTxt(fname)
print MT.order_1_output(n)
#print MT.order_2_output(n)
