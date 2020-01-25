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
from ncl.condition import Condition
from ncl.action import Action
from ncl.connectorparam import ConnectorParam

class CausalConnector(AbstractElement):

    def __init__(self, id, condition, action):
        listAttributes = ["id"]
        listChildren = [Condition, Action, ConnectorParam]
        super().__init__("causalConnector", listAttributes, listChildren)
        self.set("id", id)
        self.add(condition)
        self.add(action)

    def add(self, nclComponent):
        if isinstance(nclComponent, Condition):
            if len(self._getListChildren()[Condition]) > 0:
                raise Exception("Is not possible add more of one Condition in CausalConnector")
        if isinstance(nclComponent, Action):
            if len(self._getListChildren()[Action]) > 0:
                raise Exception("Is not possible add more of one Action in CausalConnector")
        return super().add(nclComponent)

    #TODO Still need setup logic to caudalConnector and need update tu user Condition when this class will created

    pass
