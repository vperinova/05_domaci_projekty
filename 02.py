from turtle import forward, left, right

def domecek(velikost):
    uhlopricka = velikost*2**0.5
    forward(velikost)
    left(135)
    forward(uhlopricka)
    left(135)
    forward(velikost)
    left(135)
    forward(uhlopricka)
    left(135)
    forward(velikost)
    right(135)
    forward(uhlopricka*0.5)
    right(90)
    forward(uhlopricka*0.5)
    right(45)
    forward(velikost)
    left(90)
    forward(velikost*1.5)
    
if __name__=='__main__':
    domecek(20)
    domecek(30)
    domecek(40)
    