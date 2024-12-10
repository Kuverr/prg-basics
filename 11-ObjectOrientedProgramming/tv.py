class TV:
    def __init__(self):
        self.is_on = False
        self.channel = 1
        self.volume = 0
        self.channels = {}

    def program_channel(self, name):
        if not self.channels:
            self.channels[1] = name
        else:
            for key in self.channels.keys():
                if not self.channels[key+1]:
                    self.channels[key+1] = name

    def inc_vol(self):
        if 0 <= self.volume < 10:
            self.volume += 1
    
    def dec_vol(self):
        if 0 < self.volume <= 10:
            self.volume -= 1

    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False

    def available_channels(self):
        for i, j in self.channels.items():
            print(i,'. ',j)

    def set_channel(self, channel):
        self.channel = channel
        print(f'Set channel to: {self.channels[self.channel]}')

    def show_status(self):
        status = 'On' if self.is_on else 'Off'
        print(f'TV is {status}, Volume level is {self.volume}', end=", ")
        print(f'Selected channel: {self.channel}. {self.channels[self.channel]}') 