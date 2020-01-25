#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Michael Bittencourt <mchl.bittencourt@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
from abc import ABC, abstractmethod
from ncl.connectorrole import ConnectorRole

class Simple(ConnectorRole):

    @abstractmethod
    def __init__(self, role, eventType=None, delay=None, min=None, max=None, qualifier=None):
        super().__init__(role, eventType)
        listAttributes = ["delay", "min", "max", "qualifier"]
        self._appendAttributes(listAttributes)
        if delay is not None:
            self.set("delay", delay)
        if min is not None:
            self.set("min", min)
        if max is not None:
            self.set("max", max)
        if qualifier is not None:
            self.set("qualifier", qualifier)

    pass

