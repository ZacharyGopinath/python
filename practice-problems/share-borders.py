from countryinfo import CountryInfo

print('Enter the names of 2 countries to find if they share borders!`')

countryA = input('First Country: ')
countryB = input('Second Country: ')

dataA = CountryInfo(countryA)
bordersA = dataA.borders()

dataB = CountryInfo(countryB)
bordersB = dataB.borders()

matching = []

for i in range(len(bordersA)):
    if bordersA[i] in bordersB:
        matching.append(bordersA[i])
if len(matching):
    print('These countries share borders with: ' + str(matching))
else:
    print('These countries share no borders!')