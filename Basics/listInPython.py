s = input()
dicts = {}
for i in s:
    dicts[i] = s.count(i)
for key , value in dicts.items():
    print(key,value)
print(dicts)