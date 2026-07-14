def login(username, password):
    print(username, password)


data = ["admin", "12345"]
login(data[0], data[1])


login(*data)


user = {
    "username": "admin",
    "password": "12345"
}

login(**user)