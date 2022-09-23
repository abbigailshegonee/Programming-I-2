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

def main():

    kt = ktools()
    kt.mtl(1)
    kt.mput(1)
    kt.ta()
    kt.mtl(2)
    kt.mput(2)
    kt.ta()
    kt.mm(2)
    kt.tlm(1)
    kt.tl()
    kt.mput(3)
    kt.ta()
    kt.mm(3)
    kt.tl()
    kt.mm(6)

    pass


if __name__ == "__main__":
    run_karel_program()