f = open('faculty.csv','r')
lines = f.readlines()
f.close()

#q6
faculty_dict = {}
for line in lines[1:]:
    items = line[:-1].split(',')
    k = items[0].split()[-1]
    v = items[1:]
    v[0] = v[0].lstrip()
    v[1] = v[1][:v[1].index('Professor')+9]
    if faculty_dict.get(k,None):
        faculty_dict[k].append(v)
    else:
        faculty_dict[k] = [v]

result = []
for k in faculty_dict.keys()[:3]:
    result.append((k,faculty_dict[k]))
print result
print ""

#q7
faculty_dict = {}
for line in lines[1:]:
    items = line[:-1].split(',')
    k = (items[0].split()[0],items[0].split()[-1])
    v = items[1:]
    v[0] = v[0].lstrip()
    v[1] = v[1][:v[1].index('Professor')+9]
    if faculty_dict.get(k,None):
        faculty_dict[k].append(v)
    else:
        faculty_dict[k] = [v]

result = []
for k in faculty_dict.keys()[:3]:
    result.append((k,faculty_dict[k]))
print result
print ""

#q8
ks = faculty_dict.keys()
print sorted(ks,key=lambda k: k[1])
