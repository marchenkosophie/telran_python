shopping_cart = ['orange', 'peach', 'lemon']
empty_list = []
mixed = [2, 'orange', 4.22, True]

fruits = ['apple', 'pear', 'banana']
print(fruits)
print(fruits[0])

fruits[0] = 'banana'

print(fruits)

list1 = ['orange', 'peach']
list2 = ['shampoo', 'soap']
comb_list = list1 + list2
print(comb_list)

fruits = ['orange', 'peach', 'banana']

first, second, third = fruits

print(first)
print(second)
print(third)


fruits = ['apple', 'pear', 'banana']

for item in fruits:
    print(f"item in fruits: {item}")


correct_answers = ['orange', 'peach', 'banana']
user_answers = ['orange', 'peach', 'banana']

if correct_answers == user_answers:
    print("Correct")
else:
    print("Some answers were not correct")


print(len(fruits))


print(max(fruits))


numbers = [1, 22, 344, 0, 52]

print(max(numbers))
print(min(numbers))


res = sorted(numbers)
print(res)
print(numbers)


print(sorted(numbers, reverse=True))
print(sorted(fruits, reverse=True))

word = 'python'
print(sorted(word))

result = ''.join(sorted(word))
print(result)

names = ['Alexander', 'Bob', 'Tom']
print(sorted(names))
print(sorted(names, key=len))


fruits = ['apple', 'peach', 'banana']
fruits.append('orange')
print(fruits)

fruits.insert(1, 'melon')
print(fruits)


fruits.pop(2)
print(fruits)

numbers = [10,20,30]
deleted = numbers.pop(1)
print(deleted)
print(numbers)
