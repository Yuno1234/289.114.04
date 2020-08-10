x = 0
xspeed = 10
y = 0
yspeed = 10
logo = None

def setup():
    global logo
    size(800, 800)
    logo = loadImage('dvd-logo.png')
    
def draw():
    global x, xspeed, y, yspeed
    background('#000000')
    image(logo, x, y)
    x += xspeed
    y += yspeed
    
    if y > height-45 or y < 0:
        yspeed *= -1
    
    if x > height-100 or x < 0:
        xspeed *= -1
        

    
    
