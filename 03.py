from turtle import left, right, forward
from math import atan, pi

def domecek(vyska, sirka):
    'Nakresli domecek o dane vysce a sirce'
    uhlopricka = (vyska**2 + sirka**2)**0.5
    uhel = atan(vyska/sirka)*180/pi
    forward(sirka)
    left(90)
    forward(vyska)
    left(90)
    forward(sirka)
    left(90)
    forward(vyska)
    left(90+uhel)
    forward(uhlopricka)
    left(180-2*uhel)
    forward(uhlopricka/2)
    left(2*uhel)
    forward(uhlopricka/2)
    left(180-2*uhel)
    forward(uhlopricka)
    left(uhel)
    forward(sirka*1.5)
    
if __name__=='__main__':
    domecek(20,30)
    domecek(40,30)
    domecek(50,50)
     