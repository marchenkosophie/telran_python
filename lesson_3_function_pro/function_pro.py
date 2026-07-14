def greet(name):
    return f'Hello, {name}!'


res = greet('Sophie')
print(res)

# result_1 = greet()
# print(result_1)

def create_user(name, role = "user"):
    return {
        'name': name,
        'role': role
    }


print(create_user('Sophie'))

print(create_user("Sophie", "admin"))

print()

def calculate_discount(price, discount_percent=10):
    return price - (price * discount_percent / 100)


print(calculate_discount(1000))

print(calculate_discount(1000, 25))

#
# def foo(a=1, b):
#     return a + b
#
# print(foo(5))


def add_test_result(name, results = None):
    if results is None:
        results = []
    results.append(name)
    return results


print(add_test_result("test_login"))


print(add_test_result("test_logout"))


def create_user_1(username, email, role):
    return f"{username} ({email}) - {role}"


print(create_user_1("Sophie", "sophie@gmail.com", "admin"))

print(create_user_1(role = "admin", username = "Sophie", email = "sophie@gmail.com"))

print(create_user_1("Sophie", role = "user", email = "sophie@gmail.com"))