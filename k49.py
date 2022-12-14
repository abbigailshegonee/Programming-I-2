from stanfordkarel import *
from time import sleep


class ktools:
  def m(self):
    """shorthand for move"""
    move()
    
  def tl(self):
    """turn left"""
    turn_left()

  def tr(self):
    """turn right"""
    self.tl()
    self.tl()
    self.tl()

  def ta(self):
    """turn around"""
    self.tl()
    self.tl()

  def pick(self):
    """pick beeper"""
    pick_beeper()

  def put(self):
    """put beeper"""
    put_beeper()

  def put2(self):
    """put 2 beepers in a line"""
    self.put()
    self.m()
    self.put()

  def put5(self):
    """put 5 beepers in a line"""
    self.put2()
    self.m()
    self.put2()
    self.m()
    self.put()

  def h(self):
    """Print H using beepers"""
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.m()
    self.m()
    self.tr()
    self.put5()
    self.ta()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.put2()
    self.tl()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.m()
    self.m()
    self.m()
    
  def fic(self) -> bool:
    """front is clear"""
    return front_is_clear()
    
    
  def fib(self) -> bool:
    """front is blocked"""
    return not self.fic()


  def ric(self) -> bool:
    """right is clear"""
    self.tr()
    if self.fic():
      self.tl()
      return True  #ends function there
    self.tl()
    return False
    

  
  def rib(self) -> bool:
    """right is blocked"""
    return not self.ric()

  
  def mazemove(self):
    """maze move"""
    if self.fib():
      self.tl()
    else:   #otherwise...
      self.m()
      if self.ric():
        self.tr()
        self.m()
        if self.ric():
          self.tr()
          self.m()
    pass

def main():
    kt = ktools()
    kt.m()
    kt.tl()
    kt.m()
    kt.mazemove()
    sleep(3)
    
    kt.m()
    kt.m()
    kt.m()
    kt.m()
    kt.mazemove()
    sleep(3)

    kt.m()
    kt.tr()
    kt.m()
    kt.tr()
    kt.m()
    kt.m()
    kt.tr()
    kt.m()
    kt.tl()
    kt.m()
    kt.m()
    kt.m()
    kt.m()
    kt.tl()
    kt.mazemove()
    sleep(3)

    kt.ta()
    kt.m()
    kt.tl()
    kt.m()
    kt.m()
    kt.m()
    kt.m()
    kt.m()
    kt.m()
    kt.ta()
    kt.mazemove()
    sleep(3)
    
    
    pass


if __name__ == "__main__":
    run_karel_program()