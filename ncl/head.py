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
from ncl.regionbase import RegionBase
from ncl.descriptorbase import DescriptorBase
from ncl.connectorbase import ConnectorBase

class Head(AbstractElement):

    def __init__(self):
        listAttributes = []
        listChildren = [RegionBase, DescriptorBase, ConnectorBase]
        super().__init__("head", listAttributes, listChildren)
        self.add(RegionBase())
        self.add(DescriptorBase())
        self.add(ConnectorBase())

    #TODO Still need add all childrens to head tag

    pass
