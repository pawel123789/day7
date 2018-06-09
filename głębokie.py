import copy

inner = {1: 'foo', 2: 'bar'}
outer = {'a': inner, 'b': 2}
outer2 = dict(outer)
print(outer)
print(outer2)


inner = {1:'foo', 2: 'bar'}
outer2['b'] = 3
print(outer)
print(outer2)
outer2['a'][1] = 'baz'
print(outer)
print(outer2)
print(inner[1])
