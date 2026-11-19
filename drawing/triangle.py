# pyright: basic

from .util import overload_points


def _draw_scanline(self, x_start, x_end, y):
  if x_start > x_end:
    x_start, x_end = x_end, x_start

  for x in range(x_start, x_end + 1):
    self.set_pixel(x, y)
def _fill_flat_bottom(self, x1, y1, x2, y2, x3, y3):
    invslope1 = (x2 - x1) / (y2 - y1) if y2 != y1 else 0
    invslope2 = (x3 - x1) / (y3 - y1) if y3 != y1 else 0

    curx1 = x1
    curx2 = x1

    y = int(y1)
    while y <= int(y2):
        self._draw_scanline(int(curx1), int(curx2), y)
        curx1 += invslope1
        curx2 += invslope2
        y += 1
def _fill_flat_top(self, x1, y1, x2, y2, x3, y3):
    invslope1 = (x3 - x1) / (y3 - y1) if y3 != y1 else 0
    invslope2 = (x3 - x2) / (y3 - y2) if y3 != y2 else 0

    curx1 = x3
    curx2 = x3

    y = int(y3)
    while y > int(y1):
        self._draw_scanline(int(curx1), int(curx2), y)
        curx1 -= invslope1
        curx2 -= invslope2
        y -= 1


def htriangle(self, x1,y1,x2,y2,x3,y3):
  self.line(x1,y1,x2,y2)
  self.line(x2,y2,x3,y3)
  self.line(x3,y3,x1,y1)

def triangle(self, x1, y1, x2, y2, x3, y3):
    # Sort vertices by y (y1 <= y2 <= y3)
    if y1 > y2:
        x1, y1, x2, y2 = x2, y2, x1, y1
    if y1 > y3:
        x1, y1, x3, y3 = x3, y3, x1, y1
    if y2 > y3:
        x2, y2, x3, y3 = x3, y3, x2, y2

    # Flat-bottom
    if y2 == y3:
        self._fill_flat_bottom(x1, y1, x2, y2, x3, y3)

    # Flat-top
    elif y1 == y2:
        self._fill_flat_top(x1, y1, x2, y2, x3, y3)

    else:
        # Split triangle
        t = (y2 - y1) / (y3 - y1)
        x4 = x1 + t * (x3 - x1)
        y4 = y2

        self._fill_flat_bottom(x1, y1, x2, y2, x4, y4)
        self._fill_flat_top(x2, y2, x4, y4, x3, y3)


class TriangleMixin:
  _draw_scanline = _draw_scanline
  _fill_flat_bottom = _fill_flat_bottom
  _fill_flat_top = _fill_flat_top
  htriangle = overload_points(htriangle)
  htri = htriangle
  triangle = overload_points(triangle)
  tri = triangle

