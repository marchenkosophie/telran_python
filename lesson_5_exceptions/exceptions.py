# with open("user.json", "r", encoding = "utf-8") as file:
#     print(file.read())

#
# print("START PROGRAM")
#
# result = 10/0
#
# print(result)
#
# print("END PROGRAM")

# def div_int(a,b):
#     return a/b
#
# print("START PROGRAM")
# res = div_int(10,0)
# print(res)
# print("END PROGRAM")


# try/except
print("START PROGRAM")
try:
    result = 10/0
    print(result)
except Exception as e:
    print("An error occurred", e)