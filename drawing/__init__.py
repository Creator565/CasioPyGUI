# pyright: basic
from .line import LineMixin
from .circle import CircleMixin
from .triangle import TriangleMixin
from .quad import QuadMixin
from .rect import RectMixin

class DrawingMixin(LineMixin, CircleMixin, TriangleMixin, QuadMixin, RectMixin):
  pass

