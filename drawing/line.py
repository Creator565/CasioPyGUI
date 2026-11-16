# pyright: basic

def vline(self,x,y1,y2):
  if x<0 or x>self.w-1:
    return

  y1,y2=max(0,min(y1,y2)),min(self.h-1,max(y1,y2))

  for y in range(y1,y2+1):
    self.set_pixel(x,y)

def hline(self,y,x1,x2):
  if y<0 or y>self.h-1:
    return

  x1,x2=max(0,min(x1,x2)),min(self.w-1,max(x1,x2))

  for x in range(x1,x2+1):
    self.set_pixel(x,y)

def line(self,x1,y1,x2,y2):
  #optimizations
  if x1==x2 and y1==y2:
    self.set_pixel(x1,y1)
    return
  elif x1==x2:
    self.vline(x1,y1,y2)
    return
  elif y1==y2:
    self.hline(y1,x1,x2)
    return

  dx = abs(x2-x1)
  dy =-abs(y2-y1)
  sx = 1 if x1 < x2 else -1
  sy = 1 if y1 < y2 else -1
  err= dx+dy

  while True:
    self.set_pixel(x1,y1)

    if x1==x2 and y1==y2:
      break

    e2 = err<<1
    if e2 >= dy:
      err+=dy
      x1 +=sx
    if e2 <= dx:
      err+=dx
      y1 +=sy

class LineMixin:
    vline = vline
    hline = hline
    line = line

