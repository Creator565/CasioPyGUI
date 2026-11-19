# pyright: basic

from .util import overload_points


def rect(self,x1,y1,x2,y2):
  if min(x1, x2)>self.w-1 or max(x1,x2)<0:
        return
  if min(y1,y2)>self.h-1 or max(y1,y2)<0:
      return

  xmin=max(0,min(x1,x2))
  xmax=min(self.w-1,max(x1,x2))
  ymin=max(0,min(y1,y2))
  ymax=min(self.h-1,max(y1,y2))


  for x in range(xmin,xmax+1):
    for y in range(ymin,ymax+1):
      self.set_pixel(x,y)

def hrect(self,x1,y1,x2,y2):
  xmin=min(x1,x2)
  xmax=max(x1,x2)
  ymin=min(y1,y2)
  ymax=max(y1,y2)

  self.line(xmin,ymin,xmax,ymin)
  self.line(xmin,ymax,xmax,ymax)
  self.line(xmin,ymin,xmin,ymax)
  self.line(xmax,ymin,xmax,ymax)

class RectMixin:
  rect = overload_points(rect)
  hrect = overload_points(hrect)

