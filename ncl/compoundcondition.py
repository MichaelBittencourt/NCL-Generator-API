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
from ncl.condition import Condition
from ncl.assessment import Assessment

class CompoundCondition(Compound, Condition):

    def __init__(self, operator, delay=None):
        super().__init__(operator)
        listAttributes = ["delay"]
        listChildren = [Condition, Assessment]
        self._setTagName("compoundCondition")
        self._appendAttributes(listAttributes)
        self._appendChildren(listChildren)
        if delay is not None:
            self.set("delay", delay)

    pass

