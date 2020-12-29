users = [
    {
        'name': 'Bob',
        'status': 'active'
    },
    {
        'name': 'Jill',
        'status': 'inactive'
    }
    ,
    {
        'name': 'Rex',
        'status': 'active'
    }
]

print(users)
print(len(users))

for user in users:
    print(user["name"])
    if user['status'] == 'inactive':
        print(user['name'] + ' is inactive') 
        users.remove(user)

print(users)