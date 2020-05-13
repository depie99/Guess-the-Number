import random
javab = random.randint(1,99)
hads = int(input('what is ur hads? '))
while hads != javab :
    if hads > javab :
        print('go down')
    else :
        print('go up')
    hads = int(input('what is ur hads? '))
print ('WooOoooOwW! You Rock!')

