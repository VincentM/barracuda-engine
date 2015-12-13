from ecs import Component


class AIComponent(Component):
    def __init__(self):
        super().__init__()
        self.objective = 'Idle'
        self.last_target = None
