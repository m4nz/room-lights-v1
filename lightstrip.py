import effects as ledeffects

class LightStrip():

    def __init__(self, pixels):
        self.effect = ""
        self.numLed = 300
        self.status = False
        self.pixels = pixels
        self.colors = []

    def turnOn(self):
        self.status = True
        self.update()
        self.pixels.fill((255, 255, 255))

    def turnOff(self):
        self.status = False
        ledeffects.endEffect(self.pixels)
        self.pixels.fill((0, 0, 0))

    def setEffect(self, effect, color1, color2):
        self.colors = []
        self.effect = effect
        self.colors.append(color1)
        self.colors.append(color2)
        print(self.colors)
        #pixels, numled, colors
        ledeffects.startEffect(effect, self.pixels, self.numLed, self.colors)

    def update(self):
        if self.status:
            #self.pixels.fill((self.r, self.g, self.b))
            print('yes')
