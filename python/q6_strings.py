# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    if count<10:
        return 'Number of donuts: {0}'.format(count)
    else:
        return 'Number of donuts: many'

#for i in range(20):
#    print donuts(i)

def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    if len(s)<2:
        return ''
    else:
        return s[:2]+s[-2:]

#for el in ['spring','Hello','a','xyz']:
#    print el, both_ends(el)

def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    ns = s[0]
    for i in range(1,len(s)):
        if s[i] == s[0]:
            ns += "*"
        else:
            ns += s[i]
    return ns

#for el in ['babble','aardvark','google','donut']:
#    print el, fix_start(el)

def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    al = list(a)
    bl = list(b)
    al[1], bl[1] = bl[1], al[1]
    return ''.join(al), ''.join(bl)

#for el in [('mix', 'pod'),('dog', 'dinner'),('gnash', 'sport'),('pezzy', 'firm')]:
#    print el, mix_up(el[0],el[1])

def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    if len(s)>=3:
        if s[-3:]=='ing':
            s+='ly'
        else:
            s+='ing'
    return s

#for s in ['hail','swiming','do']:
#    print s, verbing(s)

def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    if "not" in s and "bad" in s and s.index("not")<s.index("bad"):
        return s[:s.index("not")]+"good"+s[s.index("bad")+3:]
    else:
        return s

#for s in ['This movie is not so bad',
#          'This dinner is not that bad!',
#          'This tea is not hot',
#          "It's bad yet not"
#          ]:
#    print s, not_bad(s)

def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    ah = (len(a)+1)/2
    bh = (len(b)+1)/2
    return a[:ah]+b[:bh]+a[ah:]+b[bh:]

#for el in [('abcd', 'xy'),('abcde', 'xyz'),('Kitten', 'Donut')]:
#    print el, front_back(el[0],el[1])
