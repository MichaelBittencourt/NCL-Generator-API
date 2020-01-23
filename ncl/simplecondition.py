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

class SimpleCondition(AbstractElement):

    def __init__(self, role, delay=None, eventType=None, key=None, transition=None, min=None, max=None, qualifier=None):
        listAttributes = ["role", "delay", "eventType", "key", "transition", "min", "max", "qualifier"]
        super().__init__("simpleCondition", listAttributes, [])
        self.set("role", role)
        if delay is not None:
            self.set("delay", delay)
        if eventType is not None:
            self.set("eventType", eventType)
        if key is not None:
            self.set("key", key)
        if transition is not None:
            self.set("transition", transition)
        if min is not None:
            self.set("min", min)
        if max is not None:
            self.set("max", max)
        if qualifier is not None:
            self.set("qualifier", qualifier)

    pass
