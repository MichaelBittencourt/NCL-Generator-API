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
from ncl.assessment import Assessment

class CompoundStatement(Compound, Assessment):

    def __init__(self, operator, isNegated=None):
        super().__init__(operator)
        listAttributes = ["isNegated"]
        listChildren = [Assessment]
        self._setTagName("compoundStatement")
        self._appendAttributes(listAttributes)
        self._appendChildren(listChildren)
        if isNegated is not None:
            self.set("isNegated", isNegated)

    pass

