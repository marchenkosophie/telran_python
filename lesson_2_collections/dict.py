books = {
    'Harry Potter':'J.K.Rowling',
    'To kill a mockingbird':'Harper Lee'
}


books1 = {
    'Harry Potter'
    'To kill a mockingbird'
}

print(books1)

response = {
    'status':'success',
    'user':{'id':1,'name':'Sophie'},
}


print(response['user']['name'])


data = [1,22,3]
print(isinstance(data, list))


value = 10
print(isinstance(value, (int, float)))


team_ages = {
    "Alex":23,
    "Viki":42,
    "Petr":52,
    "Dan":32,
    "Olga":26
}

print(team_ages.keys())

print(team_ages.values())


team_names = ["Alex", "Viki", "Petr", "Dan", "Olga"]
team_numbers = [23, 43, 25, 52, 32]
team_ages = {name:age for name, age in zip(team_names, team_numbers)}
print(team_ages)
