#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Player import Player
from code.Enemy import Enemy
from code.Background import Background


class EntityFactory:
    def get_entity(self, entity_type: str):
        if entity_type == "player":
            return Player("Player", None, None)
        elif entity_type == "enemy":
            return Enemy("Enemy", None, None)
        elif entity_type == "background":
            return Background("Background", None, None)
        else:
            raise ValueError(f"Unknown entity type: {entity_type}")
