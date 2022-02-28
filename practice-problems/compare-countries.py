from countryinfo import CountryInfo

print('Enter the names📚of 2 countries🏳️ / 🏴 to compare their areas📏 and populations👥!')

countryA = input('First Country: ')
countryB = input('Second Country: ')

dataA = CountryInfo(countryA)
areaA = dataA.area()
popA = dataA.population()

dataB = CountryInfo(countryB)
areaB = dataB.area()
popB = dataB.population()

if areaA > areaB:
    print(countryA + ' has a larger area😤, and')
else:
    print(countryB +' has a larger area😤, and')

if popA > popB:
    print(countryA + ' has a larger population💪')
else:
    print(countryB + ' has a larger population💪')