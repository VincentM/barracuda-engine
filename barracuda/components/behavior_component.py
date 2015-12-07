from enum import Enum
from ecs import Component


BehaviorActions = Enum('Actions', 'hit heal')


class BehaviorComponent(Component):


    def __init__(self):
        super().__init__()
        self._action = None
        self._target = None
        self.last_target = None


    def hit(self, entity):
        self._action = BehaviorActions.hit
        self._target = entity


    def heal(self, entity):
        self._action = BehaviorActions.heal
        self._target = entity


    def reset(self):
        self._action = None
        self._target = None
