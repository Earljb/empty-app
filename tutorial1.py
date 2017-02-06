from ggame import App, Color, LineStyle, Sprite
from ggame import CircleAsset

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)

list(range(0, 360, 10))
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 
150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 
280, 290, 300, 310, 320, 330, 340, 350]

[x/2 for x in range(0, 360, 10)]

thinline = LineStyle(1, black)
mycircle = CircleAsset(5, thinline, blue)
xcoordinates = range(100, 600, 10)

# Generate a list of sprites that form a line!
sprites = [Sprite(mycircle, (x+600, x*1 + 150)) for x in xcoordinates]
sprites = [Sprite(mycircle, (x*(-1)+1250, x+150)) for x in xcoordinates]

myapp = App()
myapp.run()