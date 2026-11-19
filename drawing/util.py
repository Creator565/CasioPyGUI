# pyright: basic

def overload_points(f):
  def wrapper(self,*args, **kwargs):
    deconstructed=[]
    i = 0
    while i < len(args):
      try:
        x,y=args[i]
        i+=1
      except TypeError:
        x,y=args[i],args[i+1]
        i+=2

      deconstructed.append(x)
      deconstructed.append(y)

    f(self,*deconstructed,**kwargs)

  return wrapper
