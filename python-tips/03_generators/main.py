import time
def generator_function():
    for i in range(10):
        yield i

# for item in generator_function():
#     print(item)

def fibon_generator(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

def fibon_normal(n):
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result

start_generator = time.time()
for x in fibon_generator(1000):
    print(x)
end_generator = time.time()

start = time.time()
for x in fibon_normal(1000):
    print(x)
    pass
end = time.time()
print(f"Fibon generator: {end_generator - start_generator}")   
print(f"Fibon normal: {end - start}")

# Fibon generator: 0.0017981529235839844
# Fibon normal: 0.03443789482116699

def generator_function():
    for i in range(3):
        yield i

gen = generator_function()
print(next(gen))
# Output: 0
print(next(gen))
# Output: 1
print(next(gen))
# Output: 2
try:
    print(next(gen))
except StopIteration:
    print("StopIteration")
# Output: Traceback (most recent call last):
#            File "<stdin>", line 1, in <module>
#         StopIteration
my_string = "Yasoob"
try: 
    next(my_string)
except TypeError:
    print("TypeError")
# Output: Traceback (most recent call last):
#      File "<stdin>", line 1, in <module>
#    TypeError: str object is not an iterator
int_var = 1779
try:
    iter(int_var)
except TypeError:
    print("TypeError")
# Output: Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'int' object is not iterable
# This is because int is not iterable

my_string = "Yasoob"
my_iter = iter(my_string)
print(next(my_iter))
# Output: 'Y'