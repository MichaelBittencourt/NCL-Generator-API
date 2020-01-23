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
from ncl.simplecondition import SimpleCondition

class CompoundCondition(AbstractElement):

    def __init__(self, operator, delay=None):
        listAttributes = ["operator", "delay"]
        """ TODO: Still need add CompoundStatement and AssessmentStatement """
        listChildren = [CompoundCondition, SimpleCondition]
        super().__init__("compoundCondition", listAttributes, listChildren)
        self.set("operator", operator)
        if delay is not None:
            self.set("delay", delay)

    pass

