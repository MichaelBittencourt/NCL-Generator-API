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
        listChildren = [AttributeAssessment, ValueAssessment]
        super().__init__("assessmentStatement", listAttributes, listChildren)
        self.set("comparator", comparator)
        self.add(attributeAssessment)
        self.add(value)
                
    def add(self, nclComponent):
        tempList = self._getListChildren()
        if len(tempList[AttributeAssessment]) + len(tempList[ValueAssessment]) >= 2:
            return False
        if isinstance(nclComponent, (int, float, bool, str)):
            nclComponent = ValueAssessment(nclComponent)
        super().add(nclComponent)


class ValueAssessment(AbstractElement):

    def __init__(self, value):
        listAttributes = ["value"]
        listChildren = []
        super().__init__("valueAssessment", listAttributes, listChildren)
        self.set("value", value)

    pass
