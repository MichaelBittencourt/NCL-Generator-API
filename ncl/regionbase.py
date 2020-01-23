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
from ncl.region import Region

class RegionBase(AbstractElement):

    def __init__(self):
        listAttributes = []
        listChildren = [Region]
        super().__init__("regionBase", listAttributes, listChildren)

    pass
