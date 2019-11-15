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
from ncl.simpleaction import SimpleAction

class CompoundAction:

    listActions = []

    def __init__(self):
        self.listActions = []

    def getElement(self):
        compoundAction = etree.Element("compoundAction")
        for i in self.listActions:
            compoundAction.append(i.getElement())
        return compoundAction
        
    def add(self, nclComponent):
        if isinstance(nclComponent, CompoundAction) or isinstance(nclComponent, SimpleAction):
            self.listConditions.append(nclComponent)

    def generate(self):
        print("Constructor call generate")

    pass

