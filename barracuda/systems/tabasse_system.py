from ecs import System

from barracuda.components import StatusComponent
from barracuda import events


class TabasseSystem(System):

    def __init__(self):
        super().__init__()
        self._actions = []

        @events.action_event.connect
        def _action_event(sender, action, target=None):
            self._actions.append((sender, action, target))

        self._action_event = _action_event

    def update(self, dt):
        actions = self._actions
        self._actions = []
        for sender, action, target in actions:
            if target:
                target_status = self.entity_manager.component_for_entity(
                    target, StatusComponent)
                if target_status.dead:
                    continue
                if isinstance(action, events.AttackAction):
                    target_status.health -= action.power
                    if target_status.health <= 0:
                        target_status.dead = True
                        target_status.health = 0
                        print("%s est mort" % target_status.name)
                elif isinstance(action, events.HealAction):
                    target_status.health += action.power
                    if target_status.health > 100:
                        target_status.health = 100
