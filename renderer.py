# pyright: basic
from . import PLATFORM
from .screen import Screen
from .colors import colors
if PLATFORM=="PC":
  import pygame
elif PLATFORM=="CASIO":
  import casioplot as cp

class Renderer:
  def __init__(self, w=128, h=64):
    self.w = w
    self.h = h

    if PLATFORM=="PC":
      pygame.init()
      pygame.display.set_mode((w,h), pygame.RESIZABLE)

      self._screens=[Screen(w,h)]
      self._active_screen = self._screens[0]
      self.active_screen_id = 0

  def get_pixel(self,x,y):
    return self._active_screen.get_pixel(x,y)

  def set_pixel(self,x,y,color=colors.black):
    self._active_screen.set_pixel(x,y,color)

  def clear_screen(self,color=colors.white):
    self._active_screen.clear_screen(color)

  def show_screen(self):
    self._active_screen.show_screen()

  def is_open(self):
    return self._active_screen.is_open

  def set_active_screen(self, id):
    self._active_screen = self._screens[id]

    self.active_screen_id = id
    self.w = self._active_screen.w
    self.h = self._active_screen.h

  def get_active_screen(self):
    return self._active_screen

  def get_screen(self, id):
    return self._screens[id]

  def get_screens(self):
    return self._screens

  def create_screen(self, w=128, h=64):
    self._screens.append(Screen(w,h))
    # id of new screen
    return len(self._screens)-1

  def delete_screen(self, id):
    if id == 0:
      raise ValueError("Cannot remove screen 0")

    if id == self.active_screen_id:
      self.set_active_screen(id-1)

    # pyright thinks Screen is a list i think
    self._screens[id] = None  # pyright: ignore[reportCallIssue, reportArgumentType]

  def circle(self,*args,**kwargs):
    self._active_screen.circle(*args,**kwargs)
  def hcircle(self,*args,**kwargs):
    self._active_screen.hcircle(*args,**kwargs)

