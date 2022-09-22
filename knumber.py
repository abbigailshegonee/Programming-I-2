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

  
  def mm(self, num):
    """multiple move easy"""
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

  def n1(self):
    """number 1 in beepers"""
    self.tl()
    self.m()
    self.tr()
    self.m()
    self.put()
    self.m()
    self.tl()
    self.putm(5)
    self.tl()
    self.m()
    self.put()
    self.tl()
    self.mm(4)
    self.tl()
    self.mm(2)
    self.put()
    self.m()


  def n0(self):
    """number 0 in beepers"""
    self.m()
    self.tl()
    self.putm(5)
    self.tr()
    self.m()
    self.put()
    self.m()
    self.tr()
    self.putm(5)
    self.tr()
    self.m()
    self.put()
    self.ta()
    self.mm(2)
    

  def m0(self, num):
    "multiple 0s in beepers"
    for _ in range(0, num):
      self.n0()
    

def main():
  
    kt = ktools()
    kt.n1()
    kt.m0(9)
    
    pass


if __name__ == "__main__":
    run_karel_program()