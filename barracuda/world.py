import ecs
import pickle

from barracuda.systems import AISystem, RenderSystem, TabasseSystem


class World:

    def __init__(self):
        self.entity_manager = ecs.EntityManager()
        self._build_system_manager()

    def _build_system_manager(self):
        self.system_manager = ecs.SystemManager(self.entity_manager)
        self.system_manager.add_system(AISystem())
        self.system_manager.add_system(RenderSystem())
        self.system_manager.add_system(TabasseSystem())

    def step(self, dt):
        self.system_manager.update(dt)

    def save(self, name='save.gf'):
        with open(name, 'wb') as fd:
            pickle.dump(self.entity_manager, fd)

    def load(self, name='save.gf'):
        with open(name, 'rb') as fd:
            self.entity_manager = pickle.load(fd)
        self._build_system_manager()
