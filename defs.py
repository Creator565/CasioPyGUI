# pyright: basic

class Vec2:
  def __init__(self,x,y):
    self.x=x
    self.y=y

  def __iter__(self):
    yield self.x
    yield self.y

  def __getitem__(self, i):
    if i==0:
      return self.x
    elif i==1:
      return self.y
    else:
      raise IndexError("Index "+str(i)+" out of range for Vec2")

  def __len__(self):
    return 2

  def __repr__(self):
    return "(x:"+str(self.x)+",y:"+str(self.y)+")"


class Point(Vec2):
  pass

