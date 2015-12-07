from ecs import System

from barracuda.components import RenderComponent, StatusComponent, AIComponent


class RenderSystem(System):
    def __init__(self):
        super().__init__()
        self._round = 1

    def update(self, dt):
        print(" === Round %s ===" % self._round)
        for entity, render in self.entity_manager.pairs_for_type(RenderComponent):
            status = self.entity_manager.component_for_entity(
                entity, StatusComponent)
            ai = self.entity_manager.component_for_entity(
                entity, AIComponent) or 'Idle'
            print("[%s]%s (%s%%) - %s" % (status.team, status.name,
                                          status.health, ai.objective))
        print()
        self._round += 1
