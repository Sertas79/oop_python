# Класс TV с тестовым кодом # класс TV

class TV():
    def __init__(self):
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
oTV = TV() # создаем ТВ-объект

# включаем телевизор и показываем статус
oTV.power()
oTV.showInfo()

# Дважды меняем канал, дважды увеличиваем громкость, показываем статус
oTV.channelUp()
oTV.channelUp()
oTV.volumeUp()
oTV.volumeUp()
oTV.showInfo()

# Выключаем телевизор, показываем статус, включаем телвизор,
# показываем статус
oTV.power()
oTV.showInfo()
oTV.power()
oTV.showInfo()

# Убавляем громкость, отключаем звук, показываем состояние
oTV.volumeDown()
oTV.mute()
oTV.showInfo()

# Переключаем канал на 11, отключаем звук, показываем состояние
oTV.setChannel(11)
oTV.mute()
oTV.showInfo()