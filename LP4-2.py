def main():
  weight = int(input("Enter package weight in kilograms: "))
  length = int(input("Enter package length in centimeters: "))
  width = int(input("Enter package width in centimeters: "))
  height = int(input("Enter package height in centimeters: "))
  packageSize = int(length * width * height)
  if (weight > 27) and (packageSize > 100000):
    print("Too heavy and too large.")
  elif (weight > 27):
    print("Too heavy.")
  elif (packageSize > 100000):
    print("Too large.")
  else:
    print("Invalid measurment")
  pass


if __name__ == "__main__":
  main()