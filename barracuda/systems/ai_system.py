from ecs import System

from barracuda.components import BehaviorComponent, AIComponent


class AISystem(System):

    def update(self, dt):
        for entity, ai in self.entity_manager.pairs_for_type(AIComponent):
            # Do something here...
            behavior = self.entity_manager.component_for_entity(
                entity, BehaviorComponent)
            ai.objective = "J'ai pêché ! Je m'absous !"
            behavior.hit(entity)
