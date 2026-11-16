# pyright: basic

def quad(self,x1,y1,x2,y2,x3,y3,x4,y4):
  d_13_in=max(x1,x3)<max(x2,x4)
  d_13_in=d_13_in and (max(y1,y3)<max(y2,y4))
  if d_13_in:
    self.triangle(x1,y1,x2,y2,x3,y3)
    self.triangle(x3,y3,x4,y4,x1,y1)
  else:
    self.triangle(x1,y1,x2,y2,x4,y4)
    self.triangle(x2,y2,x3,y3,x4,y4)

def hquad(self,x1,y1,x2,y2,x3,y3,x4,y4):
  self.line(x1,y1,x2,y2)
  self.line(x2,y2,x3,y3)
  self.line(x3,y3,x4,y4)
  self.line(x4,y4,x1,y1)

class QuadMixin:
  quad = quad
  hquad = hquad

