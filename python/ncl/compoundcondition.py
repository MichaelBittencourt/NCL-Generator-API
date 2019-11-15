#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Michael Bittencourt <mchl.bittencourt@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
from lxml import etree
from ncl.simplecondition import SimpleCondition

class CompoundCondition:

    operator = None
    listConditions = []

    def __init__(self, operator):
        self.operator = operator
        self.listConditions = []

    def getElement(self):
        compoundCondition = etree.Element("compoundCondition")
        compoundCondition.set("operator", self.operator)
        for i in self.listConditions:
            compoundCondition.append(i.getElement())
        return compoundCondition
        
    def add(self, nclComponent):
        if isinstance(nclComponent, CompoundCondition) or isinstance(nclComponent, SimpleCondition) or isinstance(nclComponent, CompoundCondition) or isinstance(nclComponent, SimpleCondition):
            self.listConditions.append(nclComponent)

    def generate(self):
        print("Constructor call generate")

    pass

