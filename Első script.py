import time
i = 0

"""
while i <= 10:
    print("Hülye mindenki", end = '') #v, b, r, t
    time.sleep(1) #másodperc
    i += 1
"""

for x in range(0, 3601):
    print(i, ':', x)
    if(x == 60):
       i=i+1
       x=x-60
    if(x == 120):
      i=i+1
      x=x-60
    if(x == 180):
      i=i+1
      x=x-60
    if(x == 240):
      i=i+1
      x=x-60
    if(x == 300):
      i=i+1
      x=x-60
    if(x == 360):
      i=i+1
      x=x-60
    if(x == 420):
      i=i+1
      x=x-60
    if(x == 480):
      i=i+1
      x=x-60
    if(x == 540):
      i=i+1
      x=x-60
    if(x == 600):
      i=i+1
      x=x-60

  
    
