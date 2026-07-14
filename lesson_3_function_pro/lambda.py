def double(x):
    return x*2

double_lambda = lambda x: x*2


print(double(5))
print(double_lambda(5))


print()

add = lambda a,b: a+b
print(add(5,6))

is_even = lambda x:x%2==0
print(is_even(5))