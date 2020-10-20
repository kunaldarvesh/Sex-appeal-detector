#A Program to classify your score as Dateable
Relat = input('How many relationships?: ')
Dur = input('How many months togther on average?: ')

Relationship = int(Relat)
Duration = int(Dur)

try:
    dateTime = (Relationship * Duration)
except:
    print('input a valid number')
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
