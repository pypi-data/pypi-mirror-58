# SmartWrappers
A Python 3 library to manipulate objects with shared mutable wrappers.

Installing
----------

**Python 3.6.8 or higher is required**

To install the library, you can just run the following command:

```shell script
# Linux/macOS
python3 -m pip install -U smartwrappers

# Windows
py -3 -m pip install -U smartwrappers
```

Cases to use
--------------

```python
# We cannot change immutable objects.
# Trying to change them we just create other objects.
    
def plus_five(x):
    x += 5  # Creating another object here.
        
x = 1
plus_five(x)
print(x)  # >>> 1
    
# Standard solution: rewrite our code in a way our function
# calculates a new value and then we just reassign it to variables
# whose values we need to change.
    
def get_plus_five(x):
    return x + 5
    
x = 1
x = get_plus_five(x)
print(x)  # >>> 6
```

What if we have many objects of the same value and want them to have common state?

```python
a = 1
b = a
c = b
# ...
    
a = get_plus_five(a)
# What about b, c and other links
# at different places of our project?
```

Usage
--------------
We can use smart wrappers for that purpose:

```python
from smartwrappers import wrap
    
a = wrap(1)  # or explicitly a = SmartWrapper(1)
b = a
c = b
    
print(a())  # >>> 1
print(b())  # >>> 1
print(c())  # >>> 1
    
a(5)
print(a())  # >>> 5
print(b())  # >>> 5
print(c())  # >>> 5
    
def plus_five(x):
    x(x() + 5)
    
plus_five(a)
print(a())  # >>> 10
print(b())  # >>> 10
print(c())  # >>> 10
```
    
Matrices
--------------
We can use smart wrappers for wrapping lists:

```python
from smartwrappers import wrap_list
    
a = wrap_list([1, 2, 3])
b = [a[0], a[1], a[2]]
print(a)  # >>> [1, 2, 3]
print(b)  # >>> [1, 2, 3]
    
a[1] = 'a'
print(a)  # >>> [1, 'a', 3]
print(b)  # >>> [1, 'a', 3] => wrappers behave like references to mutable content.
```

We can wrap lists with any levels of dimensions:

```python
a = wrap_list([[1, 2], [3, 4]], dimensions=2)
b = [[a[0][0], a[1][0]], [a[0][1], a[1][1]]]  # Transposed matrix.
    
#  a is:
#        1 2
#        3 4
#  b is transposed matrix a:
#        1 3
#        2 4
    
a[0][1](0)
    
#  a is:
#        1 0
#        3 4
#  b keeps changes:
#        1 3
#        0 4
```

If we don't want to put inside our wrapper values of different types we can use StrictSmartWrapper:

```python
from smartwrappers import wrap_strictly

a = wrap_strictly('hello', str)
a('world')  # OK.
a(5)  # Error.
b = wrap_strictly('hello', int)  # Error.
```