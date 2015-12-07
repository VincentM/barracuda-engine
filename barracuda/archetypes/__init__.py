from barracuda import components


def create_actor(entity_manager, team, name):
    actor = entity_manager.create_entity()
    entity_manager.add_component(actor, components.AIComponent())
    entity_manager.add_component(actor, components.BehaviorComponent())
    entity_manager.add_component(actor, components.RenderComponent())
    entity_manager.add_component(actor, components.StatusComponent(team, name))
    return actor
