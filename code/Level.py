#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window: pygame.Surface, name: str):
        self.window = window
        self.name = name
        self.entity_list = []
        self.factory = EntityFactory()

    def run(self):
        # Exemplo de loop do nível
        running = True
        while running:
            self.window.fill((0, 0, 0))  # fundo preto
            for entity in self.entity_list:
                self.window.blit(entity.surf, entity.rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
