# pyright: basic

def circle(self,x,y,r):
  xmin=x-r
  xmax=x+r
  ymin=y-r
  ymax=y+r

  for cx in range(xmin,xmax+1):
    for cy in range(ymin,ymax+1):
      if abs(x-cx)**2+abs(y-cy)**2 <= r**2:
        self.set_pixel(cx,cy)

def hcircle(self,cx,cy,r):
  x=0
  y=r
  d=1-r
  while x <= y:
    self.set_pixel(x+cx,y+cy)
    self.set_pixel(-x+cx,y+cy)
    self.set_pixel(x+cx,-y+cy)
    self.set_pixel(-x+cx,-y+cy)
    self.set_pixel(y+cx,x+cy)
    self.set_pixel(-y+cx,x+cy)
    self.set_pixel(y+cx,-x+cy)
    self.set_pixel(-y+cx,-x+cy)

    if d < 0:
      d += 2*x + 3
    else:
      d += 2*(x-y)+5
      y-=1

    x+=1

class CircleMixin:
  def circle(self,*args):
    if len(args)==3:
      x=args[0]
      y=args[1]
      r=args[2]
    elif len(args)==2:
      x,y=args[0]
      r=args[1]

    circle(self,x,y,r)

  def hcircle(self,*args):
    if len(args)==3:
      x=args[0]
      y=args[1]
      r=args[2]
    elif len(args)==2:
      x,y=args[0]
      r=args[1]

    hcircle(self,x,y,r)

