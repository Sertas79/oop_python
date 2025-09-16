# Два объекта TV с вызовами к их методам
class TV():
    def __init__(self, brand, location):
        self.brand = brand
        self.location = location
        self.isOn = False
        self.isMuted = False
        # Некий список каналов по умолчанию
        self.channelList = [2, 4, 5, 7, 9, 11, 20, 36, 44, 54, 65]
        self.nChannels = len(self.channelList)
        self.channelIndex = 0
        self.VOLUME_MINIMUM = 0 # константа
        self.VOLUME_MAXIMUM = 10 # константа
        self.volume = 5 # целочисленная переменная

    def power(self):
        self.isOn = not self.isOn # переключатель

    def volumeUp(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False # изменение громкости включает звук
                                 # если тот выыключен
        if self.volume < self.VOLUME_MAXIMUM:
            self.volume = self.volume + 1

    def volumeDown(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False # изменение громкости включает звук
                                 # если тот выыключен
        if self.volume > self.VOLUME_MINIMUM:
            self.volume = self.volume + 1  

    def channelUp(self):
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex + 1
        if self.channelIndex > self.nChannels:
            self.channelIndex = 0   # после последнего канала вернуться
                                    # к первому каналу

    def channelDown(self):
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex - 1
        if self.channelIndex < 0:
            self.channelIndex = self.nChannels - 1  # перед первым 
                                                    # каналом - последний

    def mute(self):
        if not self.isOn:
            return
        self.isMuted = not self.isMuted

    def setChannel(self, newChannel):
        if newChannel in self.channelList:
            self.channelIndex = self.channelList.index(newChannel)
    # если newChannel нет в нашем списке каналов, ничего не делать

    def showInfo(self):
        print()
        print('TV Status:')
        print('Staus of TV:', self.brand)
        print(' Location:', self.location)
        if self.isOn:
            print('     TV is: On')
            print('     Channel is:', self.channelList[self.channelIndex])
            if self.isMuted:
                print('     Volume is:', self.volume, '(sound is muted)')
            else:
                print('     Volume is:', self.volume)
        else:
            print('     TV is: Off')

# Основной код 
oTV1 = TV('Samsung', 'Family room') # создаем один объект TV
oTV2 = TV('Sony', 'Bedroom') # создаем еще один объект TV

# включаем телевизоры
oTV1.power()
oTV2.power()

# Увеличиваем громкость TV1
oTV1.volumeUp()
oTV1.volumeUp()

# Увеличиваем громкость TV2
oTV2.volumeUp()
oTV2.volumeUp()
oTV2.volumeUp()
oTV2.volumeUp()
oTV2.volumeUp()

# Переключаем канал TV2, затем отключаем звук
oTV2.setChannel(44)
oTV2.mute()

# Теперь отображаем состояние обоих телевизоров
oTV1.showInfo()
oTV2.showInfo()
