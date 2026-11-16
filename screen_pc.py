# pyright: basic
import pygame
from .colors import *
from .drawing import DrawingMixin

class Screen(DrawingMixin):
  def __init__(self, w=128, h=64):
    self.w = w
    self.h = h

    self.is_open=True

    self.buf = pygame.Surface((w,h))
    self.buf.fill(VWHITE)

  def get_pixel(self, x, y):
    px = self.buf.get_at((x,y))
    if px[0]==VBLACK[0]:
      return CBLACK
    else:
      return CWHITE

  def set_pixel(self, x, y, color=CBLACK):
    if color==CBLACK:
      self.buf.set_at((x,y), VBLACK)
    elif color==CWHITE:
      self.buf.set_at((x,y), VWHITE)
    elif color==CINVERT:
      if self.get_pixel(x,y)==CBLACK:
        self.buf.set_at((x,y), VWHITE)
      else:
        self.buf.set_at((x,y), VBLACK)


  def clear_screen(self, color=CWHITE):
    if color==CWHITE:
      self.buf.fill(VWHITE)
    elif color==CBLACK:
      self.buf.fill(VBLACK)
    elif color==CINVERT:
      for x in range(self.w):
        for y in range(self.h):
          self.set_pixel(x,y,CINVERT)

  # assumes pygame has already been initialized
  def show_screen(self):
    for e in pygame.event.get():
      if e.type == pygame.QUIT:
        self.is_open = False

      screen = pygame.display.get_surface()
      pygame.transform.scale(self.buf, screen.get_size(), screen)
      pygame.display.flip()


