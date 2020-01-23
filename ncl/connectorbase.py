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
from ncl.causalconnector import CausalConnector

class ConnectorBase(AbstractElement):

    def __init__(self):
        listAttributes = []
        listChildren = [CausalConnector]
        super().__init__("connectorBase", listAttributes, listChildren)

    pass
