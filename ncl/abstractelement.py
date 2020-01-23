#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Michael Bittencourt <mchl.bittencourt@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
from lxml import etree
from abc import ABC, abstractmethod
from collections import OrderedDict


class AbstractElement(ABC):

    @abstractmethod
    def __init__(self, name, listAttributes, listChildren):
        self.name = name
        self.listAttributes = OrderedDict()
        self.listChildren = OrderedDict()
        for attribute in listAttributes:
            self.listAttributes[attribute] = None
        for child in listChildren:
            self.listChildren[child] = []

    def add(self, nclComponent):
        if type(nclComponent) in self.listChildren:
            self.listChildren[type(nclComponent)].append(nclComponent)
            return True;
        else:
            """
            I can use this to convert OrderedDict in list
            tempChildrenList = [(k, v) for k, v in self.listChildren.items()][::-1]
            for key in tempChildrenList:
            """
            couldAddElement = False;
            for key in self.listChildren:
                if self.listChildren[key] is not None:
                    for item in self.listChildren[key][::-1]: #I use a reverse list to insert new element in the more recently object
                        couldAddElement = item.add(nclComponent)
                        if couldAddElement:
                            break;
                if couldAddElement:
                    break;
            return couldAddElement;
        return False

    def set(self, attribute, value):
        if attribute in self.listAttributes:
            self.listAttributes[attribute] = value;

    def get(self, attribute):
        if attribute in self.listAttributes:
            return self.listAttributes[attribute];
        return None

    def getElement(self):
        element = etree.Element(self.name)
        for key in self.listAttributes:
            if self.listAttributes[key] is not None:
                element.set(key, self.listAttributes[key])
        for key in self.listChildren:
            if self.listChildren[key] is not None:
                for item in self.listChildren[key]:
                    element.append(item.getElement())
        return element

    def generate(self, encoding=None):
        xmlCode = self.getElement()
        return etree.tostring(xmlCode, encoding=encoding, method="xml", pretty_print=True).decode()

    pass
