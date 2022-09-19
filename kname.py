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
    self.m()
    self.tl()
    self.m()
    self.put2()
    self.m()
    self.put2()
    self.m()
    self.tr()
    self.m()
    self.put2()
    self.m()
    self.tr()
    self.m()
    self.put2()
    self.tr()
    self.m()
    self.put2()
    self.ta()
    self.m()
    self.m()
    self.tr()
    self.m()
    self.put2()
    self.tl()
    self.m()
    self.m()
    

  def b(self):
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.put2()
    self.m()
    self.tr()
    self.m()
    self.put()
    self.m()
    self.tr()
    self.m()
    self.put2()
    self.ta()
    self.m()
    self.m()
    self.tr()
    self.m()
    self.put()
    self.m()
    self.tr()
    self.m()
    self.put2()
    self.ta()
    self.m()
    self.m()
    self.m()
    self.m()
    

  def i(self):
    self.put()
    self.m()
    self.tl()
    self.put5()
    self.tl()
    self.m()
    self.put()
    self.ta()
    self.m()
    self.m()
    self.put()
    self.tr()
    self.m()
    self.m()
    self.m()
    self.m()
    self.tl()
    self.put()
    self.m()
    self.m()
    
    


  def g(self):
    self.tl()
    self.m()
    self.put2()
    self.put()
    self.m()
    self.ta()
    self.m()
    self.put2()
    self.tr()
    self.m()
    self.m()
    
    
    


  def l(self):
    self.tl()
    self.put5()
    self.ta()
    self.m()
    self.m()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.put2()
   
  

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