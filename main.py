f1 = open('1.fa', 'r')
f2 = open('2.fa', 'r')
for line in f1:
    if line[0] == '>':
        name1 = line[1:]
    else:
        s1 = line
for line in f2:
    if line[0] == '>':
        name2 = line[1:]
    else:
        s2 = line
