# How to be _Pythonic_?
Python has some very specificities, standards and ways of doing things. This it what we call the _pythonic_ way of life. But, beyond that, there are some good practices to keep in mind that are true with any programming language.

## Python and indentations
One major difference regarding other programming languages is that Python use indentations for structuring the code. No braces such as "{}", no parenthesis, only indentations:

* Function and class definitions
```python
def my_function(x, y):
    
    return x + y
```
* Loops and statements
```python
for n in range(0, 10):
    out = do_stuff(n)
```

It allows for keeping the clode very clean as every developer must respect code arrangement. However, in addition to this inherent structure, some conventions also exist, and it's very important to follow them to keep the code as clean as possible, and most of all as readable as possible.

## Python and syntax good practice
There are different rules regarding naming and syntax in Python. Look at what Pycharm tells you to see where you should modify the syntax.

### Python naming conventions
1. function, variable, method and attribute names: lower case, and a ``_`` to separate words:
* ``my_variable``, ``my_function``, ``my_method``, `my_attribute`
2. class names: only letters, all stick together, capital letter to separate words:
* ``MyClass``

### Naming good practices
A good variable is a variable that does not need comment. A good code is the same: a good code is a self-documented code. For instance, what does the following code do ?
```python
def get(alist):
    another_list = []
    for n in alist:
	if n[0] == 4:
	    another_list.append(n)
    return another_list
```
It is hard to tell, as names are not self descriptives. Now, look at the same code below:
```python
def get_flagged_cells(series):
    flagged_cells = []
    for cell in series:
        if cell[STATUS_VALUE] == FLAGGED:
	    flagged_cells.append(cell)
    return flagged_cells
```

## Decorators
The decorators are specific to Python. They are meta-functions used to _decorate_ existing functions. Typically, they wrap a given function to enhance its behavior. First things first, the following syntax is the same:
```python
@decorate
def target():
    print('running target()')
```
or
```python
def target():
    print('running target()')

target = decorate(target)
```
Generally, the first syntax is preferred, but both have the same result. See this [example](./examples/decorator_example.py) to see the way a decorator might be used.
