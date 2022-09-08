"""
import time

while i <= 10:
    print("Hülye mindenki", end = '') #v, b, r, t
    time.sleep(1) #másodperc
    i += 1
"""
import time
i = 0

for x in range(0, 3601):
    print(i, ':', x)
    time.sleep(0.25)
    e = x % 60
    if 60 > x:
        i = 0
    elif e == 0:
        i+=1
