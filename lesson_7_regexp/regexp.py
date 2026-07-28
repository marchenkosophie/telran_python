import re

text = "The test status is passed"
result = re.search("passed", text)
print(result)

print(result.group())

text1 = "passed: test_login"
text2 = "test_login:passed"

print(re.match("passed", text1))
print(re.match("passed", text2))


print()

print(re.fullmatch("passed", "passed"))
print(re.fullmatch("passed", "passed!"))


print()

print(re.search("c.t", "cat"))
print(re.search("c.t", "cut"))
print(re.search("c.t", "ct"))
print(re.search("c.t", "coat"))


print()

print(re.search("^Test", "Test login page"))
print(re.search("^Test", "Login test page"))

print()

print(re.search("passed$", "test_login: passed"))
print(re.search("passed$", "passed: test_login"))

print()

print(re.search("gr[ae]y", "grey"))
print(re.search("gr[ae]y", "gray"))
print(re.search("gr[ae]y", "green"))

print()

print(re.search("[a-z]", "Hello"))
print(re.search("[0-9]", "Order #42"))
print(re.search("[A-Za-z0-9]", "Order #42"))

print()

print(re.search("[^0-9]", "123456a"))
print(re.search("[^0-9]", "123456"))
print(re.search("[^0-9]", "12.3456"))

print()


print(re.search(pattern=r"\d", string="Order #42"))

print(re.search(pattern=r"\w", string="!!!hello"))

print(re.search(pattern=r"\s", string="no spaces here"))

print()


print(re.search(r"ab*c", "ac"))
print(re.search(r"ab*c", "abc"))
print(re.search(r"ab*c", "abbbbbbbbbbbc"))

print()

print(re.search(r"ab+c", "ac"))
print(re.search(r"ab+c", "abc"))
print(re.search(r"ab+c", "abbbbbbbbbbbc"))

print()

print(re.search(r"colou?r", "color"))
print(re.search(r"colou?r", "colour"))
print(re.search(r"colou?r", "colouur"))

print()

print(re.search(r"\d{3}", "12"))
print(re.search(r"\d{3}", "1566562"))

print()

print(re.search(r"\d{2,4}", "123456"))
print(re.search(r"\d{2,4}", "1"))

