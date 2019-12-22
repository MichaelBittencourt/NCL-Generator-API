#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Michael Bittencourt <mchl.bittencourt@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
from ncl.abstractelement import AbstractElement

class Property(AbstractElement):

    def __init__(self, name, value=None, externable=None):
        super().__init__("property", ["name", "value", "externable"], [])
        self.set("name", name)
        if value is not None:
            self.set("value", value)
        if externable is not None:
            self.set("externable", externable)

    pass
