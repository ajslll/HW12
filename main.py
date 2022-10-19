'''from pickle import dump
list = [
    {
        'project': 'Modern House',
        'worker': 'Anton',
        'price': '300'
    },
    {
        'project': 'School',
        'worker': 'Anna',
        'price': '500'
    },
    {
        'project': 'Restaurant',
        'worker': 'Sasha',
        'price': '300'
    }
]'''

#2

from json import dump
A = {'key': 1, 'key2': True}
B = {'key': 'Hello'}
C = {'key': [1, 'Hello'], 'key2': True}
for i, j in B.items():
    if not C.get(i):
        C[i] = j
    else:
        C[i] = [C[i], j]
with open('result.json', 'w') as j:
    dump(C, j)
