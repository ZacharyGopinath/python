a = int(input('A-value: '))
b = int(input('B-value: '))
c = int(input('C-value: '))

discrim = (b ** 2) - 4 * a * c

if discrim > 0:
    print('2 solutions')
elif discrim == 0:
    print('1 solution')
else:
    print('0 solutions')