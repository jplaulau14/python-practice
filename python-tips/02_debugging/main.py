import pdb

def make_bread():
    pdb.set_trace()
    return "I don't have time"

def complicated_function():
    for i in range(1000):
        make_bread()

print(complicated_function())