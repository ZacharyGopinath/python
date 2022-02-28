a = {
    'Mercury': 3.7,
    'Venus': 8.87,
    'Earth': 9.81,
    'Mars': 3.711,
    'Jupiter': 24.79,
    'Saturn': 10.44,
    'Uranus': 8.69,
    'Neptune': 11.15
}

planetA = input('Planet A: ')
planetB = input('Planet B: ')
weight = input('Weight: ')

newWeight = round(float(weight) / a[planetA] * a[planetB], 2)
print(newWeight)

#eg planetA = Venus, planetB = Jupiter, weight = 75, expected output = 209.61