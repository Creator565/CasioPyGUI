# pyright: basic

# walmart enum
class colors:
  white=0
  black=1
  invert=-1

  class values:
    white=(255,255,255)
    black=(0,0,0)


# gint style aliases
CWHITE=colors.white
CBLACK=colors.black
CINVERT=colors.invert

VWHITE=colors.values.white
VBLACK=colors.values.black
