#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Michael Bittencourt <mchl.bittencourt@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
from ncl.condition import Condition
from ncl.simple import Simple

class SimpleCondition(Simple, Condition):

    def __init__(self, role, delay=None, eventType=None, key=None, transition=None, min=None, max=None, qualifier=None):
        super().__init__(role, eventType, delay, min, max, qualifier)
        listAttributes = ["key", "transition"]
        self._setTagName("simpleCondition")
        self._appendAttributes(listAttributes)
        if key is not None:
            self.set("key", key)
        if transition is not None:
            self.set("transition", transition)

    pass
