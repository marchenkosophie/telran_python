name = 'Alice'
age = 30

formatted_string = f"Hello my name is {name} and I am {age} years old"
print(formatted_string)


# ********************

# find()

s = "HelloHello"
st = 'ell'
print(s.find(st))
print(s.rfind(st))
print(s.find('add'))

# *****************************

# count(sub[start,end])
print(s.count(st))
print(s.count(st, 4))
print(s.count(st, 4, 10))

# *****************************

# str.upper()
# str.lower()

s = 'Abrakadabraabrakadabra'

print(s.lower())
print(s.upper())
print(s)

# *****************************

#split()

s = 'Cat, Dog, Hamster, Rabbit, Pig'
print(s.split())
print(s.split(','))

print(s.split(',', 2))


# *******************************

# rjust() & ljust()

s = "Hi!"

print(s.rjust(10, '*'))
print(s.ljust(10, '*'))

test = ["Login", "Cart", "API"]

for t in test:
    print(t.ljust(15), "OK")

order = "125"

print(order.rjust(8, "0"))



s = 'Qwerty'
print(s.isalpha())


print(s.isdigit())

# *******************************


# index()

text = "QA automation with python"
pos = text.index("automation")
print(pos)


# *******************************


# replace()
text = "I like Java"
print(text.replace("Java", "Python"))


text = "2026-07-03"

new_text = text.replace("-", "/")

print(text)

print(new_text)