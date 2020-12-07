# Imperative programming paradigms
Python is an _imperative_ programming language in which statements are made by a user to change the state of the program. The imperative paradigm is basically divided into two branches:
* Procedural
* Object-oriented

## Procedural programming
Procedures (routines, sub-routines or functions) typically contain a series of computational steps to be carried out.

### Functions
Functions allow for encapsulating routines that you often call in your code.

1. Structure
The basic structure of a function in Python is the following:
```python
def my_function(required_arguments, *args, **kwargs):
    return output_arguments
```
This is not mandatory to return anything, especially if the function performs file operations. However, it will almost always return something, at least to tell if the operation performed well. 

2. Arguments
* Required arguments (`required_arguments`): positional arguments that are mandatory to execute the function
* `*args`: optional arguments
* `**kwargs`: keyword optional arguments


## Object-oriented programming

```python
class MyClass:

    def __init__(self, *args, **kwargs):
        """ Class instance constructor

        """

    def method_1(self, *args, **kwargs):
        """ A method

        """

    def method_2(self, *args, **kwargs):
        """ Another method

        """
```
