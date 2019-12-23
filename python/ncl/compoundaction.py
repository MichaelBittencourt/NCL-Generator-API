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
from ncl.simpleaction import SimpleAction

class CompoundAction(AbstractElement):

    def __init__(self, operator, delay=None):
        listAttributes = ["operator", "delay"]
        listChildren = [CompoundAction, SimpleAction]
        super().__init__("compoundAction", listAttributes, listChildren)
        self.set("operator", operator)
        if delay is not None:
            self.set("delay", delay)

    pass

