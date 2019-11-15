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
from ncl.compoundcondition import CompoundCondition
from ncl.simplecondition import SimpleCondition
from ncl.compoundaction import CompoundAction
from ncl.simpleaction import SimpleAction

class CausalConnector:

    id = None
    condition = None
    action = None

    def __init__(self, id, condition, action):
        self.id = id
        if isinstance(condition, CompoundCondition) or isinstance(condition, SimpleCondition):
            self.condition = condition
        else:
            self.condition = None
        if isinstance(action, CompoundAction) or isinstance(action, SimpleAction):
            print("Add action")
            self.action = action
        else:
            self.action = None

    def getElement(self):
        connector = etree.Element("causalConnector", id=self.id)
        if self.condition is not None:
            connector.append(self.condition.getElement())
        if self.action is not None:
            connector.append(self.action.getElement())
        return connector

    def generate(self):
        print("Constructor call generate")

    pass
