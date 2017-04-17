from random import randrange
preved = {'kamen':0, 'nuzky':1, 'papir':2, 0:'kamen', 1:'nuzky', 2:'papir'}

def tah_hrace():
    while True:
        vstup = input('Kamen, nuzky nebo papir? ').strip().lower()
        if vstup in ['kamen','nuzky','papir']:
            return(preved[vstup])
        else:
            print('Neco se pokazilo :( Zkus to znovu!')

def tah_pocitace():
    return(randrange(3))
     
        
def hra():
    tah = (tah_hrace(), tah_pocitace())
    print('Zahral jsi {}'.format(preved[tah[0]]))
    print('Tvuj protivnik zahral {}'.format(preved[tah[1]]))
    if tah[0] == tah[1]:
        print('A je to remiza!')
    elif tah in [(0,1),(1,2),(2,0)]:
        print('Vyhral jsi!')
    else:
        print('Prohral jsi!')    
    
def ano_nebo_ne(): 
    pokracovat = input('Jeste jednou?').strip().lower()
    if pokracovat == 'ano' or pokracovat == 'a':
        return(True)
    elif pokracovat == 'ne' or pokracovat == 'n':
        return(False)
    else:
        print('Nerozumím :(')
        ano_nebo_ne()    
    print()
    
if __name__ == '__main__':
    while True:
        hra()
        if not ano_nebo_ne():
            break
    

