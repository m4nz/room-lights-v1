#Python file to hold all effects
import time
import neopixel

class checker():
    def __init__(self):
        self.rainbow = bool
        self.colorwipe = bool

    def turnOff(self):
        self.rainbow = False
        self.colorwipe = False
        print('successfully turned off')

    def setColorWipeStat(self, on):
        self.colorwipe = on

    def colorWipeStat(self):
        return self.colorwipe

    def setRainbowStat(self, on):
        self.rainbow = on

    def rainbowStat(self):
        return self.rainbow


on = checker()
#, pixels, numled, colors
def startEffect(effect, pixels, numled, colors):
    endEffect(pixels)
    print(colors)
    if effect == "colorwipe":
        on.setColorWipeStat(True)
        ColorWipe(pixels, numled, colors)
    if effect == "rainbow":
        on.setRainbowStat(True)
        RainbowCycle(5, pixels)
    if effect == "static":
        pixels.fill(colors[0])

def endEffect(pixels):
    print('off triggered')
    on.setRainbowStat(False)
    on.setColorWipeStat(False)
    pixels.fill((0, 0, 0))

#pixels, numled, colors
def ColorWipe(pixels, numled, colors):
    print("colorwipe triggered")
    i = 0
    pixels.fill((0, 0, 0))
    print(on.colorWipeStat())
    while on.colorWipeStat():
        if not on.colorWipeStat():
            break
        print('Running Colorwipe')
        for color in range(0, len(colors)):
            #tupcol = tuple(colors[color])
            #(int(tupcol[0]), int(tupcol[1]), int(tupcol[2]))
            if not on.colorWipeStat():
                break
            for i in range(0, numled):
                pixels[i] = colors[color]
                if not on.colorWipeStat():
                    break
    pixels.fill((0, 0, 0))
    return print("Color wipe end")


def RainbowCycle(speed, pixels):
    print("rainbow cycle triggered")
    while on.rainbowStat():
        print('Running Rainbowcycle')
        for b in range(0, 255, speed):
            pixels.fill((255, b, 0))
            if not on.rainbowStat():
                print('we broke here 1')
                break
        if not on.rainbowStat():
            print('we broke here 2')
            break
        for r in range(255, 0, -speed):
            pixels.fill((r, 255, 0))
            if not on.rainbowStat():
                break
        if not on.rainbowStat():
            break
        for g in range(0, 255, speed):
            pixels.fill((0, 255, g))
            if not on.rainbowStat():
                break
        if not on.rainbowStat():
            break
        for b in range(255, 0, -speed):
            pixels.fill((0, b, 255))
            if not on.rainbowStat():
                break
        if not on.rainbowStat():
            break
        for r in range(0, 255, speed):
            pixels.fill((r, 0, 255))
            if not on.rainbowStat():
                break
        if not on.rainbowStat():
            break
        for g in range(255, 0, -speed):
            pixels.fill((255, 0, g))
            if not on.rainbowStat():
                break
        if not on.rainbowStat():
            break
    pixels.fill((0, 0, 0))
    return print('Rainbow end')


#ColorWipe([(255, 0, 0), (0, 255, 0), (0, 0, 255)])

#pixels.fill((0, 0, 0))
