def main():
 z = convert(input("what time is it : "))
 if z >=7 and z<=8:
    print("breakfast time")
 if z >=12 and z <=13:
    print("lunch time")
 if z>=18 and z<=19:
    print("dinner time")

def convert(zaman):

  h,m = zaman.split(":")
  return float(h) + (float(m)/60)

if __name__ == "__main__" :
    main()