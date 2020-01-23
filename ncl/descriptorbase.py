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
from ncl.descriptor import Descriptor

class DescriptorBase(AbstractElement):

    def __init__(self):
        listAttributes = []
        listChildren = [Descriptor]
        super().__init__("descriptorBase", listAttributes, listChildren)

    pass
