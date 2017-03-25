def list_count(l):
    nl = []
    for el in list(set(l)):
        nl.append((el,l.count(el)))
    return sorted(nl,key=lambda x: x[1])

f = open("faculty.csv")
lines = f.readlines()
f.close()

degrees = []
titles = []
emails = []
for line in lines[1:]:
    items = line[:-1].split(',')
    degrees += [''.join(word.split('.')) for word in items[1].split()]

    tlist = items[2].split()
    titles.append(' '.join(tlist[:tlist.index("Professor")+1]))

    emails.append(items[-1])

#q1
print list_count(degrees) 
print ""

#q2
print list_count(titles)
print ""

#q3
print emails
print ""

#q4
print list(set([email.split("@")[1] for email in emails]))
print ""
