# forbiddenfluent

This module adds the built-in functions that work on iterables and make them
into methods in order to support a fluent programming style.  It uses the
package [forbiddenfruit](https://pypi.org/project/forbiddenfruit/) to do so, thus
the name.  The package is intended as a classroom teaching tool and talk tool,
so likely won't be expanded much.  If you like this, see [fluentpy](https://pypi.org/project/fluentpy/)
and [assertpy](https://pypi.org/project/assertpy/) for more support of this
programming style in Python.


## Installation
The package is installable via the Python Package Repository:

```
pip install forbiddenfluent
```


## Examples

```python
>>> import forbiddenfluent
>>> forbiddenfluent.curse()  # Adds methods to built-in objects in-place

>>> [1, 2, 3].map(lambda x: x * 2)
[2, 4, 6]

>>> ["Algeria", "Belgium", "Canada"].map(str.lower).filter(lambda x: len(x) > 6)
["algeria", "belgium"]

>>> [1, 2, 3].sum()
6

>>> (["Algeria", "Belgium", "Canada"]
>>>  .map(str.lower)
>>>  .filter(lambda x: len(x) > 6)
>>> )
["algeria", "belgium"]

>>> forbiddenfluent.reverse()
>>> [1, 2, 3].map(lambda x: x * 2)  ## AttributeError!

```


## Limitations
To keep use of this module simple, each method follows the convention of returning
a same-type copy of itself; That is, list.map() returns a list, set.filter() returns a
set, and so on.  This means a loss of performance benefits that relate to the lazy
iteration of normal map(list) and map(set) operations.  The author of this package
is open to adding this feature in the future, although likely other packages
for fluent programming will be a better option.
