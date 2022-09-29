from stanfordkarel import *


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
    
    
  def fid(self) -> bool:
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

  def mm(self, num):
    """move multiple"""
    for number in range(num):
      self.m()

  
  def pickm(self, num):
    """pick multiple"""
    for i in range(0, num-1):
      self.pick()
      self.m()
    self.pick()

  def putm(self, num):
    """put multiple"""
    for _ in range(0, num-1):
      self.put()
      self.m()
    self.put()

  def mput(self, num):
    """move and put beeper"""
    for i in range(0, num):
      self.m()
      self.put()

  def mtl(self, num):
    """move and turn left"""
    for i in range(0, num):
      self.m()
      self.tl()

  def tlm(self, num):
    """turn left and move"""
    for i in range(0, num):
      self.tl()
      self.m()

  def mtr(self, num):
    """move and turn right"""
    for i in range(0, num):
      self.m()
      self.tr()

  def trm(self, num):
    """turn right and move"""
    for i in range(0, num):
      self.tr()
      self.m()

  def SOB(self) -> bool:
    """standing on beeper"""
    return beepers_present()
    
  def jump(self):
    """jump for 510"""
    while self.fic():
      self.m()
    self.tl()
    while self.rib():
      self.m()
    self.tr()
    self.m()
    self.tr()
    while self.fic():
      self.m()
    self.tl()

  def find(self):
    """find for 515"""
    while not facing_north():
      self.tl()
    self.m()
    if not self.SOB():
      self.tl()
      self.m()
      self.tl()
      self.m()
    for _ in range(2):
      if not self.SOB():
        self.m()
        self.tl()
        self.m()
    pass

    def k517(self):
      """code for k517"""
      while not self.SOB():
        self.mazemove()
      self.pick()

def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.k517()
  
    pass


if __name__ == "__main__":
    run_karel_program()