from functools import namedtuple

from barracuda.components.ai_component import AIComponent
from barracuda.components.status_component import StatusComponent
# from barracuda.components.render_component import RenderComponent
from barracuda.tools import Vect2D


class PositionComponent(Vect2D):
    pass

RenderComponent = namedtuple('RenderComponent', ())
# AIComponent = namedtuple('AIComponent', ())


# __all__ = ('AIComponent', 'BehaviorComponent', 'BehaviorActions',
#            'StatusComponent', 'RenderComponent')

HealerComponent = namedtuple('HealerComponent', ('power', ))
AttackerComponent = namedtuple('AttackerComponent', ('power', ))
# AIComponent = namedtuple('AIComponent', ())
