def get_list_element(items, index):
    try:
        return items[index]
    except IndexError:
        return "Index out of range"



numbers = [10, 20, 30]
print(get_list_element(numbers, 1))

print(get_list_element(numbers, 10))



def get_user_data(users, key):
    try:
        return users[key]
    except KeyError:
        return "Key was not found"


user = {
"name": "Anna",
"age": 30
}
print(get_user_data(user, "name"))
print(get_user_data(user, "email"))



def calculate_average(first_value, second_value):
    try:
        num1 = float(first_value)
        num2 = float(second_value)
        return (num1 + num2) / 2
    except ValueError:
        return "Value must be a number"
    except TypeError:
        return "Invalid data type"


print(calculate_average("10", "20"))
print(calculate_average("hello", "20"))
print(calculate_average(None, 20))



def read_number():
    inp = input("Enter a number: ")
    try:
        int(inp)
        print("Number was entered successfully")
    except ValueError:
        print("Invalid data")
    print("Program finished")


read_number()



def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 120:
        raise ValueError("Age is not realistic")
    return age



print(validate_age(25))


try:
    validate_age(-5)
except ValueError as e:
    print(e)


try:
    validate_age(150)
except ValueError as e:
    print(e)



print("**************")

ages = [17,25,-5,150,40,300,46,119,99]


for age_ages in ages:
    try:
        print(validate_age(age_ages))
    except ValueError as e:
        print(e)