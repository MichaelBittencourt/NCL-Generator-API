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
from ncl.assessment import Assessment
from ncl.attributeassessment import AttributeAssessment


class AssessmentStatement(AbstractElement, Assessment):

    def __init__(self, comparator, attributeAssessment, value):
        listAttributes = ["comparator"]
        listChildren = [AttributeAssessment, ValueStatement]
        super().__init__("assessmentStatement", listAttributes, listChildren)
        self.set("comparator", comparator)
        self.add(attributeAssessment)
        self.add(value)
                
    def add(self, nclComponent):
        if isinstance(nclComponent, (int, float, bool, str)):
            comparedValue = ValueStatement(nclComponent)
        super().add(nclComponent)


class ValueStatement(AbstractElement):

    def __init__(self, value):
        listAttributes = ["value"]
        listChildren = []
        super().__init__("valueStatement", listAttributes, listChildren)
        self.set("value", value)

    pass
