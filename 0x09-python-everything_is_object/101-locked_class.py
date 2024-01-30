#!/usr/bin/python3
"""
class LockedClass with no class or object attribute, that prevents
the user from dynamically creating new instance attributes,
except if the new instance attribute is called first_name.
"""


class LockedClass:
    """the class"""
    def __setattr__(self, name, value):
        """setattr : to set attribute"""
        if name == "first_name":
            super().__setattr__(name, value)
        else:
            result = "'LockedClass' object has no attribute '{}'".format(name)
            raise AttributeError(result)
