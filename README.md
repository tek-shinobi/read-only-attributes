Read Only Attributes
--------------------------------------

Info:
-------------------
This package makes class attributes read only.

Motivation:
--------------------
We can make read only attributes using `@property`. But this can be verbose. __Worse, the intent is not clear as in these attributes are meant to be read-only.__
     
Like as below

```
    class MyClass:
        @property
        def x(self):
            return 'immutable 1'
        @property
        def y(self):
            return 'immutable 2'
        @property
        def z(self):
            return 'immutable 3'
        @property
        def w(self):
            return 'immutable '

```

The above can be written like so which is much less verbose and lot more explicit:

```
@read_only_attributes('x','y','z','w')
class MyClass:
    def __init__(self, x, y, z, w):
        self.x = x 
        self.y = y 
        self.z = z 
        self.w = w 
```

Once the instance attributes are assigned in the __\__init____, they cannot be changed. Trying to change them will raise an `AttributeError`.

Installation:
--------------
pipenv install read-only-properties

Usage:
------

import class decorator @read_only_attributes and use like so:

```
from roa import read_only_attributes

@read_only_attributes('x', 'y')
class MyClass:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
```
That's it. There us no need to use `@property`.  
'x' and 'y' are now readonly attributes. If we try to change them, `AttributeError` exception will be raised.  
Since 'z' is not in decorator argument list, `self.z` is a mutable instance attribute.