# Blueprint: value_if_true if condition else value_if_false

is_nice = True
state = "nice" if is_nice else "not nice"
print(state)
# Output: nice

# Blueprint: (if_test_is_false, if_test_is_true)[test]

nice = True
personality = ("mean", "nice")[nice]
print("The cat is ", personality)
# Output: The cat is nice

def my_function(real_name, optional_display_name=None):
    display_name = optional_display_name or real_name
    print(display_name)

my_function("John Doe")
# Output: John Doe
my_function("John Doe", "Johnnie")
# Output: Johnnie