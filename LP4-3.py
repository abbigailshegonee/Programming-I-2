def main():
  eggs = int(input("Enter the Number of Eggs: "))
  dozens = int(eggs/12)
  leftover = int(eggs%12)
  dozenPrice = 0
  cost = 0
  if dozens > 0 and dozens < 4:
    dozenPrice = 0.5
  if dozens >= 4 and dozens < 6:
    dozenPrice = 0.45
  if dozens >= 6 and dozens < 11:
    dozenPrice = 0.40
  if dozens >= 11:
    dozenPrice = 0.35

  cost = round((dozens * dozenPrice) + ((dozenPrice/12) * leftover), 2)

  print("The bill is equal to: ", cost)
    
  pass


if __name__ == "__main__":
  main()