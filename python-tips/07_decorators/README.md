# Advanced Guide to Python Decorators

## Introduction
Python decorators are a powerful feature for extending the behavior of functions and methods without modifying their code.

## Understanding Decorators

### Basic Decorator Structure
A decorator is a callable that takes a callable as input and returns another callable.

```python
def simple_decorator(func):
    def wrapper():
        # Pre-function logic
        result = func()  # Call the original function
        # Post-function logic
        return result
    return wrapper
```

### Using the `@` Syntax
The `@` syntax is syntactic sugar for `function = decorator(function)`.

```python
@simple_decorator
def greet():
    print("Hello, World!")

# is equivalent to

def greet():
    print("Hello, World!")
greet = simple_decorator(greet)
```

## Advanced Techniques

### Decorators with Arguments
To create a decorator with arguments, you need to create a decorator factory.

```python
def decorator_with_args(decorator_arg1, decorator_arg2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Decorator logic using decorator_arg1 and decorator_arg2
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

### Function Introspection
Use `functools.wraps` to preserve the original function's information like name, docstring, etc.

```python
import functools

def introspective_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Decorator logic
        return func(*args, **kwargs)
    return wrapper
```

### Stacking Decorators
Decorators can be stacked, and they will be applied in the order they are listed.

```python
@decorator_one
@decorator_two
def function():
    pass
```

### Decorator Classes
You can also create a decorator as a class that implements `__call__`.

```python
class DecoratorClass:
    def __init__(self, func):
        functools.wraps(func)(self)
        self.func = func

    def __call__(self, *args, **kwargs):
        # Decorator logic
        return self.func(*args, **kwargs)
```

### Stateful Decorators
Use nonlocal variables or instances of classes to maintain state.

```python
def stateful_decorator():
    count = 0
    def decorator(func):
        nonlocal count
        def wrapper(*args, **kwargs):
            nonlocal count
            count += 1
            print(f"Function has been called {count} times")
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

### Decorators for Class Methods
Decorators work for class methods as well, but remember to account for the `self` argument.

```python
def method_decorator(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        # Decorator logic
        return func(self, *args, **kwargs)
    return wrapper
```

### Using Decorators to Enforce Constraints
Decorators can enforce argument types, value ranges, or other properties.

```python
def type_check(correct_type):
    def check(func):
        @functools.wraps(func)
        def wrapper(argument):
            if isinstance(argument, correct_type):
                return func(argument)
            else:
                raise TypeError(f"Argument must be {correct_type}")
        return wrapper
    return check

@type_check(int)
def process_number(value):
    print(value * 2)
```

### Debugging Decorators
Use decorators to log information useful for debugging, such as execution time, arguments passed, etc.

```python
def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")
        return value
    return wrapper
```

## Use Cases for Python Decorators

Decorators can be used in a variety of scenarios. This section explores some common use cases with actual code examples.

### Authentication and Authorization

Ensuring that a user is logged in or has the right permissions before allowing access to a specific function.

```python
import functools

def require_authentication(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated:
            raise Exception("User is not authenticated!")
        return func(*args, **kwargs)
    return wrapper

@require_authentication
def sensitive_action():
    print("Sensitive action performed.")
```

### Caching Results (Memoization)

Storing the results of expensive function calls and returning the cached result when the same inputs occur again.

```python
import functools

def memoize(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def complex_computation(x):
    # Some expensive computation here
    return x * x
```

### Input Validation

Checking inputs to a function, ensuring they are valid before proceeding with function execution.

```python
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
```

### Timing Functions

Measuring the time taken by a function to execute.

```python
import functools
import time

def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time} seconds.")
        return result
    return wrapper

@timeit
def long_running_task():
    time.sleep(2)
    print("Task completed.")
```

### Logging

Automatically logging function calls and their results for debugging or auditing purposes.

```python
import functools

def log_function_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__} called with args: {args}, kwargs: {kwargs}, returned: {result}")
        return result
    return wrapper

@log_function_call
def add(a, b):
    return a + b
```

### Rate Limiting

Limiting the number of times a function can be called within a certain time frame, useful for web APIs.

```python
import functools
from collections import defaultdict
from time import time, sleep

def rate_limiter(max_calls, time_period):
    calls = defaultdict(lambda: (0, time()))
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            identifier = args[0] if args else id(func)
            calls_count, last_time = calls[identifier]
            current_time = time()
            if calls_count >= max_calls and (current_time - last_time) < time_period:
                raise Exception("Too many calls. Try again later.")
            if (current_time - last_time) > time_period:
                calls[identifier] = (1, current_time)
            else:
                calls[identifier] = (calls_count + 1, last_time)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limiter(max_calls=3, time_period=60)
def api_call(user_id):
    print(f"API call successful for user: {user_id}")
```

These examples demonstrate the versatility of decorators in handling cross-cutting concerns across your Python applications.


## Conclusion
Decorators are a versatile tool in the Python programmer's toolkit. They provide a clear, concise way to modify the behavior of functions and methods, which can be particularly useful for cross-cutting concerns like logging, authorization, and performance monitoring.
