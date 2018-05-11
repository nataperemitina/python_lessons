#Форматы данных

import pickle
import json
import csv

data = {
    'users' : [
        {
            'id': 1,
            'name': 'Linus Torvalds',
            'skills': ('C', 'C++', 'Linux'),
            'is_developer': True,
        },
        {
            'id': 2,
            'name': 'Richard Stallman',
            'skills': ('C', 'C++', 'GNU'),
            'is_developer': True,
        },

    ]
}

# Pickle -нативный формат для python

with open('users.pickle', 'wb') as f:
    pickle.dump(data, f)

with open('users.pickle', 'rb') as f:
    readed_data = pickle.load(f)
    print('PICKLE: {}'.format(readed_data))

#нельзя дописать в pickle-файл, только заново создать

# JSON - JavaScript Object Notation

with open('users.json', 'w') as f:
    json.dump(data, f, indent=4) #indent - отступ

with open('users.json') as f:
    readed_data = json.load(f) #это глобальная область видимости (контекстный менеджер ее не создает)
    print('JSON: {}'.format(readed_data))

# CSV
"""
id;name;skills;is_developer
1;Linus Torvalds;C++,C,Linux;1
2;Richard Stallman;C,GNU;1
"""

with open('users.csv', 'w') as f:
    users = data.get('users', [])
    if users: #if empty list => Exception
        fieldnames = users[0].keys()

    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    for user in users:
        writer.writerow(user)

with open('users.csv') as f:
    reader = csv.DictReader(f)

    for row in reader:
        print('CSV: {}'.format(row))

# INI (conf, cnf)

"""
[main]
db.username = root
db.password = toor
"""

# XML - Extended Markup Language
# lxml

"""
<data>
    <users>
        <user>
            <id>1</id>
            <name>Linus Torvalds</name>
            <is_developer>1</is_developer>
            <skills>
                <skill>C++</skill>
                <skill>C</skill>
                <skill>Linux</skill>
            </skills>
        </user>
        <user id="2" name="Richard Stallman" is_developer="1"> # ( /> - если нет вложенных)
            <skills>
                <skill>C++</skill>
                <skill>C</skill>
                <skill>GNU</skill>
            </skills>
        </user>
    </users>
</data>
"""

# Yaml (yml) => Ruby

"""
services:
    nginx:
        target: ./Dockerfile.prod


"""








