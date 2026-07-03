age = 25
name = 'Ivan'

'''
int
float
str
bool
'''

said = 'She said "Hello"'

print(said)

my_string = '''This is a multi-line string.
We've wrapped the text to the next line'''

print(my_string)

raw_string = r"C:\Program Files\Marii\Python"
print(raw_string)

s1 = "Hello world"
print(type(s1))

s2 = 5
print(type(s2))

s3 = 5.
print(type(s3))

s4 = False
print(type(s4))



s1= 'Hello'
s2 = 'World'
s3 = s1+s2
print(s3)

#join()
words = ["Hello", "World", "and", "Python"]
res = " ".join(words)

print(res)


st = 'ab' * 7
print(st)


st = '*' * 50
print(st)

s1 = 'Sophie Mar'
s2 = 'Sophie'

if s2 in s1:
    print('User Sophie is in our database')
else:
    print('User Sophie not in the DB')

st = 'a'
if st == 'a' or st == 'b' or st == 'd':
    print('Yes')


if st in 'abcd':
    print('Yes')


ln = len('Hello World')
print(ln)

s1 = 'Hello World'
print(len(s1))


# ***************************

#P Y T H O N
#0 1 2 3 4 5

st = 'Python'

print(st[0])
print(st[1])
print(st[2])
print(st[3])
print(st[4])
print(st[5])



# P  Y  T  H  O  N
#-6 -5 -4 -3 -2 -1


# ************************
# my_string[start:end]

print(st[0:3])

print(st[2:5])

print(st[4:6])

my_string = "Hello World!"
every_second_char = my_string[::2]
print(every_second_char)


reversed_string = my_string[::-1]
print(reversed_string)


from_second = my_string[1::2]
print(from_second)

my_substring = my_string[1:10:3]
print(my_substring)