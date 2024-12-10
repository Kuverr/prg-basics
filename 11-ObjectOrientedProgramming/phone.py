
import time

class Phone():

    def __init__(self, brand):
        self.brand = brand
        self.date = ''
        self.alarm = ''

    def setAlarm(self, alarm):
        self.alarm = alarm
        return ''

    def getAlarm(self):
        print(self.alarm)
        return ''

    def checkBrand(self):
        print(self.brand)
        return ''

    def checkHour(self):
        self.date = time.localtime()
        return self.date

iphone = Phone('Apple')

iphone.setAlarm('1:30')


print(iphone.checkBrand())
print(iphone.getAlarm())
print(iphone.checkHour())