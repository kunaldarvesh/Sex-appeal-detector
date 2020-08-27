# Sex-appeal-detector
Python program to detect your sex appeal based on time spent in relationships

Relat = input('How many relationships?: ')
Dur = input('How many months togther on average?: ')

Relationship = int(Relat)
Duration = int(Dur)

try:
    dateTime = (Relationship * Duration)
except:
    print('input a valid number pussy')
    quit()

print('Your Total', dateTime)

if dateTime > 100:
    print('Ultra')
elif dateTime > 80:
    print('Good')
elif dateTime > 60:
    print('Average')
elif dateTime > 40:
    print('Bad')
elif dateTime > 20:
    print('Damn Bro')
else:
    print('Virgin')

