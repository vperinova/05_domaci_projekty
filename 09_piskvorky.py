symbol_hrace = 'o'
symbol_pocitace = 'o' if symbol_hrace == 'x' else 'x'

def strategie(pole):
    patterns={'x':[('-oo', 0), ('oo-', 2), ('o-o', 1),
                   ('x-x', 1), ('-xx', 0), ('xx-', 2), ('-x-', 0),
                   ('-o-', 0), ('o--', 1), ('--o', 0), 
                   ('---', 0), ('-', 0)],
              'o':[('-xx', 0), ('xx-', 2), ('x-x', 1),
                   ('o-o', 1), ('-oo', 0), ('oo-', 2), ('-o-', 0),
                   ('-x-', 0), ('x--', 1), ('--x', 0), 
                   ('---', 0), ('-', 0)]}
    
    for (combination, pozition) in patterns[symbol_hrace]:
        if pole.count(combination):
            return(pole.index(combination) + pozition)
        
            
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
    cislo_policka = strategie(pole)
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
    