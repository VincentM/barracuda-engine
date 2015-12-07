from ecs import Component


class StatusComponent(Component):

    def __init__(self, team, name):
        super().__init__()
        self.team = team
        self.name = name
        self.health = 100
        self.dead = False
