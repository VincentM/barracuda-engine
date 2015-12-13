from ecs import System

from barracuda.components import RenderComponent, StatusComponent
from barracuda import events


class RenderSystem(System):
    def __init__(self):
        super().__init__()
        self._round = 1
        self._actions = []

        @events.action_event.connect
        def _action_event(sender, action, target=None):
            self._actions.append((sender, action, target))

        self._action_event = _action_event

    def update(self, dt):
        actions = self._actions
        self._actions = []
        print(" === Round %s ===" % self._round)
        for sender, action, target in actions:
            status = self.entity_manager.component_for_entity(
                sender, StatusComponent)
            if target:
                target_status = self.entity_manager.component_for_entity(
                    target, StatusComponent)
            print(status.name, action, target_status.name)
        for entity, render in self.entity_manager.pairs_for_type(RenderComponent):
            status = self.entity_manager.component_for_entity(
                entity, StatusComponent)
            print("[%s]%s (%s%%)" % (status.team, status.name, status.health))
        print()
        self._round += 1
