from ecs import System

from barracuda.components import (
    BehaviorComponent, BehaviorActions, StatusComponent)


class TabasseSystem(System):

    def update(self, dt):
        for entity, behavior in self.entity_manager.pairs_for_type(
                BehaviorComponent):
            status = self.entity_manager.component_for_entity(
                entity, StatusComponent)
            if behavior._target:
                target_status = self.entity_manager.component_for_entity(
                    behavior._target, StatusComponent)
                if target_status.dead:
                    continue
                if behavior._action == BehaviorActions.hit:
                    target_status.health -= 5
                    if target_status.health <= 0:
                        target_status.dead = True
                        target_status.health = 0
                        print("%s est mort" % target_status.name)
                elif behavior._action == BehaviorActions.heal:
                    target_status.health += 7
                    if target_status.health > 100:
                        target_status.health = 100
                behavior.reset()
