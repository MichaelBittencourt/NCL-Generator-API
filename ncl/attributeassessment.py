#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Michael Bittencourt <mchl.bittencourt@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
from ncl.connectorrole import ConnectorRole

class AttributeAssessment(ConnectorRole):
    def __init__(self, role, eventType, key=None, attributeType=None, offset=None):
        super().__init__(role, eventType)
        listAttributes = ["key", "attributeType", "offset"]
        self._setTagName("attributeAssessment")
        self._appendAttributes(listAttributes)
        if key is not None:
            self.set("key", key)
        if attributeType is not None:
            self.set("attributeType", attributeType)
        if offset is not None:
            self.set("offset", offset)
