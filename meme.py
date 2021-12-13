option = input('Pick ur poison: ')
if (option == 'fascism'):
    temp = input()
    x = temp.split()
    a = x[0]
    b = x[2]
    z = a + b
    if (z == 'ume' or z == 'meu' or z == 'uI' or z == 'Iu'):
        print('us')
elif (option == 'communism'):
    temp = input()
    x = temp.split()
    a = x[0]
    b = x[1]
    print(a,b + '??? NO!')

    if (a == 'my' or a == 'his' or a == 'her' or a == 'your' or a == 'their'):
        a = 'OUR'
    print(a, b + '!')