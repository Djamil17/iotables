import sys
with open(format(sys.argv[1])) as f:
    data = f.read()


data=data.replace('"','')
data=data.replace(', ','_')
data=data.replace('and','')
data=data.replace(' ','_')
data=data.replace('__','_')


print(data)

with open('{}.txt'.format(sys.argv[2]), "w+") as f2:
    f2.write(data)

