import functools

def validate_inputs(*validation_rules):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i, (arg, rule) in enumerate(zip(args, validation_rules)):
                if not rule(arg):
                    raise ValueError(f"Argument at index {i} does not satisfy the rule.")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_inputs(lambda x: isinstance(x, int), lambda x: x > 0)
def process_numbers(x, y):
    print(f"Processing numbers: {x}, {y}")

process_numbers(-10, 5)
process_numbers(10, -5)