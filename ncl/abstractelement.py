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
        self._name = name
        self._listAttributes = OrderedDict()
        self._listChildren = OrderedDict()
        self._appendAttributes(listAttributes)
        self._appendChildren(listChildren)

    def _setTagName(self, tagName):
        self._name = tagName

    def _appendAttributes(self, listAttributes):
        for attribute in listAttributes:
            self._listAttributes[attribute] = None

    def _appendChildren(self, listChildren):
        for child in listChildren:
            self._listChildren[child] = []

    def add(self, nclComponent):
        for item in self._listChildren:
            if isinstance(nclComponent, item):
                self._listChildren[item].append(nclComponent)
                return True;
        else:
            """
            I can use this to convert OrderedDict in list
            tempChildrenList = [(k, v) for k, v in self._listChildren.items()][::-1]
            for key in tempChildrenList:
            """
            couldAddElement = False;
            for key in self._listChildren:
                if self._listChildren[key] is not None:
                    for item in self._listChildren[key][::-1]: #I use a reverse list to insert new element in the more recently object
                        couldAddElement = item.add(nclComponent)
                        if couldAddElement:
                            break;
                if couldAddElement:
                    break;
            return couldAddElement;
        return False

    def set(self, attribute, value):
        if attribute in self._listAttributes:
            self._listAttributes[attribute] = value;

    def get(self, attribute):
        if attribute in self._listAttributes:
            return self._listAttributes[attribute];
        return None

    def getElement(self):
        element = etree.Element(self._name)
        for key in self._listAttributes:
            if self._listAttributes[key] is not None:
                element.set(key, self._listAttributes[key])
        for key in self._listChildren:
            if self._listChildren[key] is not None:
                for item in self._listChildren[key]:
                    element.append(self.customizeItem(item).getElement())
        return element

    def customizeItem(self, item):
        return item

    def generate(self, encoding=None):
        xmlCode = self.getElement()
        return etree.tostring(xmlCode, encoding=encoding, method="xml", pretty_print=True).decode()

    pass
