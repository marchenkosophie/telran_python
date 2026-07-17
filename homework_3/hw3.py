def create_profile(name, age=18, city='Unknown'):
    return {"name": name, "age": age, "city": city}


print(create_profile("Anna"))

print(create_profile("Tom", 25))
print(create_profile(city="Haifa", name="Maria"))



def sum_even_numbers(*numbers):
    if not numbers:
        return 0
    res = 0
    for n in numbers:
        if n % 2 == 0:
            res += n
    return res



print(sum_even_numbers(1, 2, 3, 4, 5, 6)) # 12
print(sum_even_numbers(7, 9)) # 0
print(sum_even_numbers()) # 0


def print_pet_info(name, **info):
    print(f"Name: {name}")
    if not info:
        print("No additional information")
    else:
        for key, value in info.items():
            print(f"{key}: {value}")



print_pet_info(
"Lucky",
age=4,
color="White",
breed="Spitz"
)

print_pet_info("Lucky")



def merge_lists(*lists):
    result = []
    for lst in lists:
        for item in lst:
            result.append(item)
    return result


print(merge_lists([1, 2],[3],[4, 5],[]))


print(merge_lists())


def build_message(*words, separator = ' '):
    return separator.join(words)

print(build_message("Lucky", "Spitz", "White", "Spitz"))