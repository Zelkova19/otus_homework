import csv
import json

with open('books.csv', 'r') as b:
    books = list(csv.DictReader(b))
    for i in books:
        del i['Publisher']

with open('users.json', 'r') as u:
    new_users = []
    for i in json.load(u):
        new_users.append(
            {'name': i.get('name'),
             'gender': i.get('gender'),
             'address': i.get('address'),
             'age': i.get('age'),
             'books': []})

while len(books) > 0:
    for i_user in new_users:
        if len(books) > 0:
            i_user['books'].append(books.pop())

with open('result.json', 'w') as r:
    result = json.dumps(new_users, indent=4)
    r.write(result)
