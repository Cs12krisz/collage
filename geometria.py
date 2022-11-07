import math

print("Négyzet számláló")
a1 = int(input("Mennyi az oldala? "))
if a1 != 0:
    nT = a1*a1
    nK = 4*a1
    print()
    print("Kerülete:", nK)
    print("Területe:", nT)
else:
    print("Nem szerkeszthető!")

print()
print("Téglalap számláló")
a2 = int(input("Mennyi az 'a' oldala? "))
b2 = int(input("Mennyi a 'b' oldala? "))
if a2 and b2 <= 2 or a2 == b2:
    print("Nem szerkeszthető!")
else:
    tT = a2*b2
    tK = 2*(a2+b2)
    print()
    print("Kerülete:", tK)
    print("Területe:", tT)

print()
print("háromszög számláló")
a3 = int(input("Mennyi az 'a' oldala? "))
b3 = int(input("Mennyi a 'b' oldala? "))
c3 = int(input("Mennyi a 'c' oldala? "))
if a3==b3==c3:
    print()
    print("Szabályos háromszög")
    hK = a3+b3+c3
    hs = (a3+b3+c3)/2
    hT = math.sqrt(hs*(hs-a3)*(hs-b3)*(hs-c3))
    print()
    print("Kerülete:", hK)
    print("Területe:", hT)

elif a3<b3+c3 and b3<a3+c3 and c3<a3+b3 and c3>a3+b3:
    print()
    print("Derékszögű háromszög")
    dhK = a3+b3+c3
    dhT = (a3*b3)/2
    print()
    print("Kerülete:", dhK)
    print("Területe:", dhT)
elif a3<b3+c3 or b3<a3+c3 or c3<a3+b3:
    print()
    print("Általános háromszög")
    hK = a3+b3+c3
    hs = (a3+b3+c3)/2
    hT = math.sqrt(hs*(hs-a3)*(hs-b3)*(hs-c3))
    print()
    print("Kerülete:", hK)
    print("Területe:", hT)
elif b3==c3:
    print()
    print("Egyenlő szárú háromszög")
    hK = a3+b3+c3
    hT = math.sqrt(hs*(hs-a3)*(hs-b3)*(hs-c3))
    print()
    print("Kerülete:", hK)
    print("Területe:", hT)
else:
    print("Nem szerkeszthető!")


print()
print("Kör számláló")
r = int(input("Mennyi a kör sugara? "))
kK = 2*r*math.pi
kT = (r*r)*math.pi
print("Kerülete:", kK)
print("Területe:", kT)

