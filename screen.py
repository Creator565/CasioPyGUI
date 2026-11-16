from . import PLATFORM

if PLATFORM=="PC":
  from .screen_pc import *
elif PLATFORM=="CASIO":
  from .screen_casio import *

