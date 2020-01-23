#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Michael Bittencourt <mchl.bittencourt@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
from ncl.abstractparam import AbstractParam

class ConnectorParam(AbstractParam):

    def __init__(self, name, type=None):
        super().__init__(name)
        self._setTagName("connectorParam")
        self._appendAttributes(["value"])
        if type is not None:
            self.set("type", type)

    pass
