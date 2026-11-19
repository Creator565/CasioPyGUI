# pyright: basic
import casioplot as cp

from .colors import *
from .drawing import DrawingMixin


class Screen(DrawingMixin):
  def __init__(self, w=128, h=64):
    self.w = w
    self.h = h

    self.x_scale = 128/self.w
    self.y_scale = 64/self.h

    # replacing the function like this improves performance
    if self.x_scale==1 and self.y_scale==1:
      self.set_pixel = self._set_pixel_native
    elif self.x_scale<1 and self.y_scale<1:
      self.set_pixel = self._set_pixel_zoomed_out
    else:
      self.set_pixel = self._set_pixel_zoomed_in

    if self.x_scale==1 and self.y_scale==1:
      self.get_pixel = self._get_pixel_native  # pyright: ignore[reportAttributeAccessIssue]
    else:
      self.get_pixel = self._get_pixel_zoomed  # pyright: ignore[reportAttributeAccessIssue]


    self.is_open=True

    # casioplot has no public screen buffer
    self._buf = []
    cp.clear_screen()

  # scale != 1
  #handles all scales
  def _get_pixel_zoomed(self, x, y):
    px = cp.get_pixel(round(x*self.x_scale),round(y*self.y_scale))
    if px[0]==VBLACK[0]:  # pyright: ignore[reportOptionalSubscript]
      return CBLACK
    else:
      return CWHITE

  # scale = 1
  #handles native scale
  def _get_pixel_native(self, x, y):
    px = cp.get_pixel(round(x),round(y))
    if px[0]==VBLACK[0]:  # pyright: ignore[reportOptionalSubscript]
      return CBLACK
    else:
      return CWHITE

  def get_pixel(self,x,y):
    # implemented in __init__
    pass

  # scale < 1
  # handles zoomed out scales
  def _set_pixel_zoomed_out(self,x,y,color=CBLACK):
    if color==CBLACK:
      cp.set_pixel(round(x*self.x_scale),round(y*self.y_scale), VBLACK)
    elif color==CWHITE:
      cp.set_pixel(round(x*self.x_scale),round(y*self.y_scale), VWHITE)
    elif color==CINVERT:
      if self.get_pixel(x,y)==CBLACK:
        cp.set_pixel(round(x*self.x_scale),round(y*self.y_scale), VWHITE)
      else:
        cp.set_pixel(round(x*self.x_scale),round(y*self.y_scale), VBLACK)

  # scale > 1
  # handles all scales
  def _set_pixel_zoomed_in(self,x,y,color=CBLACK):
    if color==CBLACK:
      for dx in range(max(1,round(self.x_scale))):
        for dy in range(max(1,round(self.y_scale))):
          cp.set_pixel(round(x*self.x_scale+dx),round(y*self.y_scale+dy), VBLACK)
    elif color==CWHITE:
      for dx in range(max(1,round(self.x_scale))):
        for dy in range(max(1,round(self.y_scale))):
          cp.set_pixel(round(x*self.x_scale+dx),round(y*self.y_scale+dy), VWHITE)
    elif color==CINVERT:
      if self.get_pixel(x,y)==CBLACK:
        self._set_pixel_zoomed_in(x,y, CWHITE)
      else:
        self._set_pixel_zoomed_in(x,y, CBLACK)

  # scale = 1
  # handles native scale
  def _set_pixel_native(self,x,y,color=CBLACK):
    if color==CBLACK:
      cp.set_pixel(round(x),round(y), VBLACK)
    elif color==CWHITE:
      cp.set_pixel(round(x),round(y), VWHITE)
    elif color==CINVERT:
      if self.get_pixel(x,y)==CBLACK:
        cp.set_pixel(round(x),round(y), VWHITE)
      else:
        cp.set_pixel(round(x),round(y), VBLACK)

  def set_pixel(self,x,y,color=CBLACK):
    # set in __init__
    pass

  def clear_screen(self, color=CWHITE):
    if color==CWHITE:
      cp.clear_screen()
    elif color==CBLACK:
      for x in range(128):
        for y in range(64):
          cp.set_pixel(x,y,VBLACK)
    elif color==CINVERT:
      for x in range(128):
        for y in range(64):
          if cp.get_pixel(x,y)[0] == VBLACK[0]:  # pyright: ignore[reportOptionalSubscript]
            cp.set_pixel(x,y,VWHITE)
          else:
            cp.set_pixel(x,y,VBLACK)

  # assumes pygame has already been initialized
  def show_screen(self):
    cp.show_screen()

