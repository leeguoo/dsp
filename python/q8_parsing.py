# -*- coding: utf-8 -*-
# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

f = open("football.csv","r")
lines = f.readlines()
f.close()

diff = 100
for line in lines[1:]:
    items = line.split(',')
    if abs(int(items[5])-int(items[6])) < diff:
        diff = abs(int(items[5])-int(items[6]))
        name = items[0]

print name
