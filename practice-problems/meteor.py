print('A meteor🗿 is heading towards you🙀, input information about the meteor🗿 and your position🗺️ to find if you will be hit🤕 or be safe😸')

m = int(input("Meteor's slope: "))
b = int(input("Meteor's Y-intercept: "))
x = int(input('Your position (x): '))
y = int(input('Your Position (y): '))

eq = (m * x) + b
if eq == y:
    print('You will be hit by the meteor!🤕')
else:
    print('You will not be hit by the meteor!😸')