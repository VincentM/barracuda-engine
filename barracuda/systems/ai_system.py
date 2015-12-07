import random

from ecs import System

from barracuda.components import BehaviorComponent, AIComponent, StatusComponent


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


    def _hit(self, target, status, behavior):
        if target:
            target_status = self.entity_manager.component_for_entity(
                target, StatusComponent)
            behavior.hit(target)
            behavior.last_target = target
            print("%s attaque %s" % (status.name, target_status.name))
            return True
        return False


    def _heal(self, status, behavior):
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
            target_status = self.entity_manager.component_for_entity(
                target, StatusComponent)
            behavior.heal(target)
            behavior.last_target = None
            print("%s soigne %s" % (status.name, target_status.name))
            return True
        return False


    def update(self, dt):
        self._computeTeams()

        for entity, ai in self.entity_manager.pairs_for_type(AIComponent):
            # Do something here...
            behavior = self.entity_manager.component_for_entity(
                entity, BehaviorComponent)

            status = self.entity_manager.component_for_entity(
                entity, StatusComponent)

            if not status.dead:
                target = None

                if behavior.last_target:
                    last_target_status = self.entity_manager.component_for_entity(
                        behavior.last_target, StatusComponent)
                    if not last_target_status.dead:
                        target = behavior.last_target
                    else:
                        target = self._choose_target(status)
                else:
                    target = self._choose_target(status)

                if status.health <= 15:
                    print("%s trop faible pour agir" % status.name)
                    continue
                elif self._heal(status, behavior):
                    continue
                elif self._hit(target, status, behavior):
                    continue
                else:
                    print("%s attend" % status.name)
