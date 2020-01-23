#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Michael Bittencourt <mchl.bittencourt@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
from ncl.compound import Compound
from ncl.action import Action

class CompoundAction(Compound, Action):

    def __init__(self, operator, delay=None):
        super().__init__(operator)
        listAttributes = ["delay"]
        listChildren = [Action]
        self._setTagName("compoundAction")
        self._appendAttributes(listAttributes)
        self._appendChildren(listChildren)
        if delay is not None:
            self.set("delay", delay)

    pass

