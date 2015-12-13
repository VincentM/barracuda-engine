from functools import namedtuple
from blinker import signal


move_event = signal('move')
action_event = signal('action')

HealAction = namedtuple('HealAction', ('power', ))
AttackAction = namedtuple('AttackAction', ('power', ))

# MoveEvent = namedtuple('MoveEvent', ('entity', 'start_pos', 'end_pos'))
# ActionEvent = namedtuple('AttackEvent', ('entity_actor', 'entity_target', 'action'))
