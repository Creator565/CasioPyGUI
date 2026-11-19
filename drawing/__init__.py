# pyright: basic
from .circle import CircleMixin
from .line import LineMixin
from .quad import QuadMixin
from .rect import RectMixin
from .triangle import TriangleMixin


class DrawingMixin(LineMixin, CircleMixin, TriangleMixin, QuadMixin, RectMixin):
  pass

