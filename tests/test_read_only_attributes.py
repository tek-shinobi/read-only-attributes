import pytest
from roa import read_only_attributes


def test_attribute_immutable_error():
    @read_only_attributes("x")
    class MyClass:
        def __init__(self, x):
            self.x = x

    mc = MyClass(1)
    with pytest.raises(AttributeError):
        mc.x = 3


def test_attribute_mutable():
    @read_only_attributes("x")
    class MyClass:
        def __init__(self, x, y):
            self.x = x

    mc = MyClass(1, 2)
    mc.y = 3
    assert mc.y == 3
