def factory(*attributes):
    """Create read-only-attributes"""

    def read_only_attributes_wrapper(cls):
        class ReadOnlyAttributesClass(cls):
            """Modified class with read only attributes"""

            def __setattr__(self, name, value):
                """https://python-reference.readthedocs.io/en/latest/docs/dunderattr/setattr.html"""
                if name not in attributes:
                    pass
                elif name not in self.__dict__:
                    pass
                else:
                    raise AttributeError("Attribute {} is readonly".format(name))
                super().__setattr__(name, value)

        return ReadOnlyAttributesClass

    return read_only_attributes_wrapper


read_only_attributes = factory
