#!/usr/bin/python
# -*- coding: utf-8 -*-

from pygame import Surface, Rect


class Entity:
    def __init__(self, name: str, surf: Surface, rect: Rect):
        self.name = name
        self.surf = surf
        self.rect = rect

    def move(self):
        pass
