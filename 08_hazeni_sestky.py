from random import randrange

countmax = (0,0)
for i in range(1,5):
    print('Hrac c. {}:'.format(i))
    count = 0
    while True:
        count += 1
        roll = randrange(1,7)
        print('{}, '.format(roll), end = '')
        if roll==6:
            if count>countmax[0]:
                countmax = (count,i)
            print()
            break
print('Vyhral hrac c.{} s {} hody.'.format(countmax[1], countmax[0]))
        