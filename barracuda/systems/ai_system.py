import random

from ecs import System

from barracuda.components import (
    AIComponent, StatusComponent, AttackerComponent, HealerComponent)
from barracuda import events


class AISystem(System):

    def _computeTeams(self):
        self.teams = {}
        for entity, status in self.entity_manager.pairs_for_type(StatusComponent):
            if not status.team in self.teams.keys():
                self.teams[status.team] = []
            if not status.dead:
                self.teams[status.team].append(entity)

    def _choose_target(self, status):
        potential_targets = []
        min_health = 100

        for team in self.teams.keys():
            if len(self.teams[team]) > 0 and not team == status.team:
                for entity in self.teams[team]:
                    entity_status = self.entity_manager.component_for_entity(
                        entity, StatusComponent)
                    if entity_status.health == min_health:
                        potential_targets.append(entity)
                    elif entity_status.health < min_health:
                        potential_targets = []
                        potential_targets.append(entity)
                        min_health = entity_status.health
        if len(potential_targets) > 0:
            index = random.randint(0, len(potential_targets) - 1)
            return potential_targets[random.randint(0, index)]
        else:
            return None

    def _hit(self, entity, status, ai, target):
        if target:
            attack = self.entity_manager.component_for_entity(
                entity, AttackerComponent)
            events.action_event.send(entity, target=target,
                                     action=events.AttackAction(attack.power))
            ai.last_target = target
            return True
        return False

    def _heal(self, entity, status, ai, target):
        potential_targets = []
        min_health = 20

        for entity in self.teams[status.team]:
            entity_status = self.entity_manager.component_for_entity(
                entity, StatusComponent)
            if entity_status.health == min_health:
                potential_targets.append(entity)
            elif entity_status.health < min_health:
                potential_targets = []
                potential_targets.append(entity)
                min_health = entity_status.health

        if len(potential_targets) > 0:
            index = random.randint(0, len(potential_targets) - 1)
            target = potential_targets[random.randint(0, index)]
            heal = self.entity_manager.component_for_entity(
                entity, HealerComponent)
            events.action_event.send(entity, target=target,
                                     action=events.HealAction(heal.power))
            ai.last_target = None
            return True
        return False

    def update(self, dt):
        self._computeTeams()

        for entity, ai in self.entity_manager.pairs_for_type(AIComponent):

            status = self.entity_manager.component_for_entity(
                entity, StatusComponent)

            if not status.dead:
                target = None

                if ai.last_target:
                    last_target_status = self.entity_manager.component_for_entity(
                        ai.last_target, StatusComponent)
                    if not last_target_status.dead:
                        target = ai.last_target
                    else:
                        target = self._choose_target(status)
                else:
                    target = self._choose_target(status)

                if status.health > 15:
                    # AI wants to do something, game engine prevent it to
                    # actually do it because it is too weak
                    if not self._heal(entity, status, ai, target):
                        self._hit(entity, status, ai, target)
