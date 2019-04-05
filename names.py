namecount = {}

f = open("names.txt", "r")

for name in f:
    name = name.strip()
    if name in namecount.keys():
        namecount[name] += 1
    else:
        namecount[name] = 1
f. close()

f = open("namelist.txt", "w")
for key in sorted(list(namecount.keys())):
    f.write("{0}\t{1}\n".format(key, namecount[key]))
f.close()