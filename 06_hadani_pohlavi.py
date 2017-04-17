prijmeni = input('Napiš své příjmení (s diakritikou): ').strip().split()
pohlavi = 'muz'
for i in prijmeni:
    if i[-1:]=='á':
        pohlavi = 'zena'
print('Pravdebodobne jsi {}.'.format(pohlavi))
     
    