#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from code.Level import Level


class Game:
    def __init__(self, window: pygame.Surface):
        self.window = window
        self.levels = []  # lista de níveis

    def run(self):
        # Exemplo simples de execução de níveis
        for level in self.levels:
            level.run()
