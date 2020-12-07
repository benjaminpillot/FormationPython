# Logical operators and indexing

## Logical operators:
When you compare any kind of data types, you may use the following logical operators:
* `==` : use to compare equality between two values - returns TRUE if both operands are equal
* `>` : greater
* `>=` : greater or equal
* `<` : lower
* `<=` : lower or equal
* `!=` : return TRUE if both operands are not equal
* `and` : logical AND - returns TRUE if both the operands are true
* `or` : logical OR - returns TRUE if either of the operand is true
* `in` : use to test if value/object is in collection
* `not` : returns TRUE if operand is false

### Examples
```python
>>> x = 23
>>> y = 50
>>> x == 30
False
>>> x > 20
True
>>> x >= 23
True
>>> x < 20
False
>>> x <= 20
False
>>> x != 40
True
>>> x == 23 and y == 50
True
>>> x == 23 and y == 4
False
>>> x == 23 or x == 50
True
>>> x in [1,8,3, "a string", [9,8], 23]
True
>>> x not in [1,8,9, 23]
False
```

## Indexing and slicing
When you want to access to somme data in a collection (list, tuple, numpy array, etc.) you may use _indexing_ and _slicing_. Indexing allows for one value to be retrieved while slicing allows for multiple values.

### Indexing
* pattern: `alist[index_value]`
    * `alist[0]` returns the __first__ value of a list
    * `alist[1]` returns the __second__ value of the list
    * `alist[-1]` returns the __last__ value of a list
    * `alist[-2]` returns the penultimate value of the list (i.e. the second value starting from the end)
    * `alist[n]` returns the n+1 value

### Slicing
* pattern: `alist[init:end:step]`
    * `alist[:]` returns a copy of the list `alist`
    * `alist[1::]` returns a list with values from index=1 to end by step=1
    * `alist[::2]` returns a list with values selected at step=2
    * `alist[-1::-1]` returns the list reverted
As its name indicates, a `slice` is a slice of a collection, that is a part of it. The following therefore returns a list with __1__ value:

```python
>>> my_list = [1,2,7,8,4]
>>> my_list[2:3]
[7]
```
So, if you split a list in two, here is how you do it:
```python
>>> my_list = [1,2,3,4,5,6]
>>> my_list[:3]
[1, 2, 3]
>>> my_list[3:]
[4, 5, 6]
```
