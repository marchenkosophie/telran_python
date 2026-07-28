import re

print(re.search(r"@", "qwerty@gmail.com"))
print(re.search(r"[\w.]+@", "qwerty@gmail.com"))
print(re.search(r"[\w.]+@\w+", "qwerty@gmail.com"))
print(re.search(r"[\w.]+@\w+\.[a-z]{2,3}", "qwerty@gmail.com"))
print(re.search(r"^[\w.]+@\w+\.[a-z]+$", "qwerty@gmail.com"))
print(re.search(r"^[\w.]+@\w+\.[a-z]+$", "qwerty@gmail.com and more text"))
