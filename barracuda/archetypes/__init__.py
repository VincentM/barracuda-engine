
def create_actor(entity_manager, system_manager):
    player = entity_manager.create_entity()
    render = RenderComponent(pyglet.sprite.Sprite(PLAYER_IMAGE))
    entity_manager.add_component(player, render)
    # coordinates = components.Coordinates()
    # entity_manager.add_component(player, coordinates)

    # Create hitbox and add it to physic system
    entity_manager.add_component(player, PhysicComponent())
    # body = pymunk.Body(1, 1666)
    # body.position = 300, 300
    # poly = pymunk.Poly.create_box(body)
    # physic_system.space.add(body, poly)
    # physic = components.Physic(body)
    # entity_manager.add_component(player, physic)

    # Build key mapping
    behavior = BehaviorComponent()
    entity_manager.add_component(player, behavior)

    input_c = InputComponent()
    input_c.add_keybind(key.LEFT, behavior.move_left)
    input_c.add_keybind(key.RIGHT, behavior.move_right)
    input_c.add_keybind(key.SPACE, behavior.jump)
    entity_manager.add_component(player, input_c)
    return player
