import pytest
from roa import ReadOnlyType


def test_attribute_immutable_error():
    class MyClass(metaclass=ReadOnlyType, ro_attrs=["x"]):
        def __init__(self, x):
            self.x = x

    mc = MyClass(1)
    assert mc.x == 1
    with pytest.raises(AttributeError):
        mc.x = 3


def test_attribute_immutable_error_static():
    class MyClass(metaclass=ReadOnlyType, ro_attrs=["x"]):
        x = 1

    mc = MyClass()
    assert mc.x == 1
    with pytest.raises(AttributeError):
        mc.x = 3


def test_attribute_not_set_error():
    class MyClass(metaclass=ReadOnlyType, ro_attrs=["x"]):
        def __init__(self, x):
            pass

    with pytest.raises(RuntimeError):
        MyClass(1)


def test_attribute_mutable():
    class MyClass(metaclass=ReadOnlyType, ro_attrs=["x"]):
        def __init__(self, x, y):
            self.x = x
            self.y = y

    mc = MyClass(1, 2)
    assert mc.y == 2
    mc.y = 3
    assert mc.y == 3
