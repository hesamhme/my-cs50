a=50
while a>0:
 print(f"amount due: {a}")
 sek = int(input("insert the coin: "))
 if sek in [25,10,5]:
  a-=sek
print(f"change owed:", abs(a))

