from random import randrange

symbol_hrace = 'x'
symbol_pocitace = 'o'

def obrana(pole):
    if pole.count('x-x'):
        return(pole.index('x-x') + 1)
    elif pole.count('-xx'):
        return(pole.index('-xx'))   
    elif pole.count('xx-'):
        return(pole.index('xx-') + 2)
    elif pole.count('x--x'):
        return(pole.index('x--x') + 1)    
    elif pole.count('-x-'):
        return(pole.index('-x-'))
    else:
        return(-1)
    
def utok1(pole):
    if pole.count('-oo'):
        return(pole.index('-oo'))
    elif pole.count('oo-'):
        return(pole.index('oo-' + 2))
    elif pole.count('o-o'):
        return(pole.index('o-o')+1)
    else:
        return(-1)
    
def utok2(pole):
    if pole.count('-o-'):
        return(pole.index('-o-'))
    elif pole.count('o--'):
        return(pole.index('o--') + 1)
    elif pole.count('--o'):
        return(pole.index('--o'))
    elif pole.count('---'):
        return(pole.index('---') + 1)
    else:
        return(pole.index('-'))
        
            
     
    
    
    
    
def vyhodnot(pole):
    if 'xxx' in pole:
        return('x')
    elif 'ooo' in pole:
        return('o')
    elif '-' not in pole:
        return('!')
    else:
        return('-')

def tah(pole, cislo_policka, symbol):
    "Vrati herni pole s danym symbolem umistenym na danou pozici"
    pole_new = pole[:cislo_policka] + symbol + pole[cislo_policka+1:]
    return(pole_new)

def tah_hrace(pole):
    while True:
        cislo_policka = int(input('Na jakou pozici chces tahnout? '))
        if cislo_policka not in range(20):
            print('Cislo musi byt mezi 0 a 20 vcetne. Zkus to znova. ')
        elif pole[cislo_policka] != '-':
            print('Zadane pole je jiz obsazene. Zkus to znova. ') 
        else:    
            return(tah(pole, cislo_policka, symbol_hrace))
        
def tah_pocitace(pole):
    "Vrati herni pole se zaznamenanym tahem pocitace"
    cislo_policka = utok1(pole)
    if cislo_policka == -1:
        cislo_policka = obrana(pole)
    if cislo_policka == -1:
        cislo_policka = utok2(pole) 
    return(tah(pole, cislo_policka, symbol_pocitace))
            

def piskovorky1d():
    pole='--------------------'
    while True:
        print(pole)
        pole = tah_hrace(pole)
        if vyhodnot(pole) != '-':
            break
        print(pole)
        pole = tah_pocitace(pole)
        if vyhodnot(pole) != '-':
            break
    print(pole)
    if vyhodnot(pole)=='!':
        print('Nikdo nevyhral ani neprohral!')
    else:
        print('Vyhral hrac s {}'.format(vyhodnot(pole)))    
        
if __name__ == '__main__':
    piskovorky1d()    
    