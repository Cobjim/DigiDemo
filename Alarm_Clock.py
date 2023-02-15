# Taken from https://stackoverflow.com/questions/68632685/alarm-clock-in-python
# Modified by Ian Coberly
from datetime import *
from time import *

timeNow = datetime.now()
currentDate = timeNow.strftime('%d/%m/%y %H:%M')
print(f'Current Date and Time is : {currentDate}')

userInputDate = 'None'
alarmDate = ''
userInput = input('Please Enter alarm time in %H:%M : ')
alarmDate = timeNow.strftime('%d/%m/%y')+ ' ' + userInput
print(f'Alarm is set to : {alarmDate}')



while True:
     
    if datetime.now().strftime('%d/%m/%y %H:%M') == alarmDate:
        print('ALARM IS RINGING')
        break
