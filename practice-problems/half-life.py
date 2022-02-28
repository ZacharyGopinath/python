mass = input('Mass of substance/g: ')

time = input('Time elapsed/yr: ')
half_life = input('Half life: ')

final_amt = float(mass) * ((0.5)**((float(time) / float(half_life))))
print('Final mass: ' + str(final_amt) + 'g')