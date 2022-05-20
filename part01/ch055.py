d = {
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": False
  }
print(type(d))
print(d['title'])

l = list(d)
print(l)
k = d.keys()
v = d.values()

print(type(k))
print(v)

for k,v in d.items():
    print(k,v)