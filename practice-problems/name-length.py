# Input a list of names and have them and have them sorted shortest to longest and longest to shortest!

num = int(input('Number of names: '))
names = []
for i in range(num):
    name_input = input('List of names: ')
    names.append(name_input)

names_sorted = sorted(names, key=len)
print('Short to Long: ' + str(names_sorted))
names_sorted.reverse()
print('Long to Short: ' + str(names_sorted))
