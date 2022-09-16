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

  def a(self):
    uhyj


  def b(self):
    wetw


  def i(self):
    tryh4t


  def g(self):
    dfger


  def l(self):
    hgtnd
   
  

def main():
    kt = ktools()
    kt.a()
    kt.b()
    kt.b()
    kt.i()
    kt.g()
    kt.a()
    kt.i()
    kt.l()
  
    pass


if __name__ == "__main__":
    run_karel_program()