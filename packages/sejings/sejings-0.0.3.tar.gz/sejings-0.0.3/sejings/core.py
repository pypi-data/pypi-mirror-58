# Created: 10/12/2019
# Author:  Emiliano Jordan,
# Project: sejings
from collections import defaultdict
from .utils import in_doctest

class Sejings:


    def __init__(self, value=None):

        super().__setattr__('_val', value)

    def __call__(self, value=...):

        if value is ...:
            return self._val

        super().__setattr__('_val', value)

    def __getattr__(self, item):

        if item == '__wrapped__' and in_doctest():
            raise AttributeError

        setattr(self, item, Sejings())
        return super().__getattribute__(item)

    def __setattr__(self, key, value):

        if key == '_val':
            super().__setattr__(key, value)
            return

        if isinstance(value, Sejings):
            super().__setattr__(key, value)
            return

        try:
            obj = super().__getattribute__(key)
            obj(value)
        except AttributeError:
            super().__setattr__(key, Sejings(value))
            return


sejings = Sejings()
