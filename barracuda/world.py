import ecs
import pickle


class World:

    def __init__(self):
        self.entity_manager = ecs.EntityManager()
        self.system_manager = ecs.SystemManager(self.entity_manager)

        # Create&register systems here
        # my_system = sysystem_managerstems.MySystem(self)
        # self.system_manager.add_system(my_system)

    def step(self, dt):
        self.system_manager.update(dt)

    def save(self, name='save.gf'):
        with open(name, 'wb') as fd:
            pickle.dump(self.entity_manager, fd)

    def load(self, name='save.gf'):
        with open(name, 'rb') as fd:
            self.entity_manager = pickle.load(fd)
