# Python main data types

## Immutable data types
* int:
```python
my_integer = 9
```
* float 
```python
my_float = 9.0
```
* boolean
```python
my_boolean = True
```
* string:
```python
# String with double quotes
my_string = "a common string"

# String with single quotes
my_string = 'another string'

# Formatted string
my_age = 35
my_string = f'I am {my_age} years old'
```

## Immutable collection
* tuple 
```python
my_tuple = (1, 2, 3)
some_value = my_tuple[2]
print(some_value)

3
```

## Mutable collections
* list:
```python
my_list = [2, "what?", ["a string", 90], (0, 7, 1)]
some_value = my_list[3]
print(some_value)

["a string", 90]
```

* dictionary 
```python
my_dictionary = {"a key": 90, "b": dict(zz=[2, 1, 9])}
some_value = my_dictionary["b"]
print(some_value)

{'zz': [2, 1, 9]}
```




## Mutable vs. immutable ?
In Python, there is an important difference between mutable and immutable data types and objects. Typically, a list is a mutable object. Let's see what happens:

```python
def my_function(alist):
    alist[0]="value has been changed"
```

```python
>>>my_list = [1, 7, 8, 3]
>>>another_list = alist
>>>print(another_list)
[1,7,8,3]
>>>my_function(my_list)
>>>print(another_list)
["value has been changed", 7, 8, 3]
```

In Python, variable are passed "by reference": it means there is no copy of the variable. The program points towards the same memory location both inside and outside the function. If an immutable object is passed to a function that manipulates it, it will be changed in place (see above). Remember that when you _assign_ a value to a variable with immutable data types (`my_variable=5`), you create a new memory block where that value is stored. __But__ when you _assign_ a mutable object to another variable (`another_list=alist=[2,3,4,5]`) you do not make a copy of it but instead point to the same memory block ! So always be careful in your programs. If you really need to manipulate a list and return a new list from it, you may use a copy by calling `new_list = old_list.copy()`.


## Objects
Objects are everywhere in Python. Everything is an object, and users might define their owns.

### A story about user-defined types
(Thanks to the free book [Think Python](http://www.greenteapress.com/thinkpython/thinkpython.pdf)) 
All previous data types are what we call "built-in" types. Now, an object is a new level of abstraction developed by an user in order to represent data in a new way. Think of a _point_ with coordinates (geographic, cartesian, etc.). There are several ways we might represent points in Python:
* We could store the coordinates separately in two variables, `x` and `y`.
* We could store the coordinates as elements in a list or tuple.
* We could create a new type to represent points as objects.

A user-defined type is also called a __class__:
```python
class Point:
    """Represents a point in 2-D space."""
```

This header indicates that the new class is a `Point` which is automatically an `object` in Python 3 (we say that `Point` inherits from `object`).

### Attributes: class own variables

You can assign values to an instance (i.e. object) using __dot notation__:
```python
>>> my_point = Point()
>>> my_point.x = 3.0
>>> my_point.y = 4.0
```

### Objects are mutable

```python
def translate_point(point, dx, dy)
    point.x += dx
    point.y += dy
```
Now, we can see how mutable objects are:
```python
>>> my_point.x
3.0
>>> my_point.y
4.0
>>> translate_point(my_point, dx=2, dy=8)
>>> my_point.x
5.0
>>> my_point.y
12.0
```

### Methods: class own functions
A _method_ is a function linked to a specific object. For example:
```python
class Car:
    
    def accelerate(self):
    """A method to make a car accelerate.
    
    """

    def brake(self):
    """A method to make a car brake
    
    """
```

Let's see the [`Time`](./FormationPython#examples/time_class.py) object example. This class gathers several concepts that we will work on later.

## Built-in objects
The `str` type in Python allows, as the `Time` object, to call some methods we would use with `int` and `float` types:
```python
>>> my_string = "a string "
>>> my_string + my_string
'a string a string'
>>> my_string * 4
'a string a string a string a string'
```
But, there is no possible division or soustraction obviously. The same exists with lists and tuples. To concatenate 2 lists, you would do the following:
```python
>>> my_list = [1,2,9,8] + [2,4,7]
>>> my_list
[1, 2, 9, 8, 2, 4, 7]
```


## Other data types

### `numpy` arrays

They are arrays of numbers, on which you may apply matrix computations. Very fast when you need to repeat some computations on every value of a raster/matrix for example. It is typically called with the `numpy.array` function:
```python
>>> import numpy as np
>>> my_array = np.array([1,9,8,7])
```
If you multiply by a scalar, you automatically multiply all elements in the array:
```python
>>> 3 * my_array
array([3, 27, 24, 21])
```
In the case of multidimensional arrays, you can even combine the powerfulness of lists and numpy arrays (as a 2D numpy array is actually a list of lists). For example, you mays multiply each line of a matrix by a vector element by element:
```python
>>> np.array([2,8,8,2]) * np.array([[1,8,7,9], [2,7,6,3], [3,7,4,5]])
array([[ 2, 64, 56, 18 ],
       [ 4, 56, 48,  6 ],
       [ 6, 56, 32, 10 ]])
```


#### Boolean indexing
Numpy arrays are especially powerful for boolean assignment and indexing:
```python
>>> m_array = np.array([2,8,8,2]) * np.array([[1,8,7,9], [2,7,6,3], [3,7,4,5]])
>>> my_array[my_array >= 40] = 0
>>> my_array
array([[ 4,  0,  0, 18 ],
       [ 2,  0,  0, 16 ],
       [ 6, 32,  0, 12 ]])
```
See also the small code [here](./FormationPython#examples/numpy_example.py)


### `pandas` dataframes and series

* dataframes
`pandas` dataframes are a specific way of reading data tables with various data types. See the small example [here](./FormationPython#examples/dataframe_example.py)

* series
`pandas` series typically stand for one-dimensional ndarray with axis labels. One common example is a time series (see example [here](./FormationPython#examples/series_example.py)).

### `geopandas` dataframes and `geoseries`

geodataframes are geographic dataframes with one column for geometry. See the small example [here](./FormationPython#examples/geopandas_example.py)