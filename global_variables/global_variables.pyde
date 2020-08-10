y = 50

def setup():
    size(500, 500)
    background('#004477')
    noFill()
    stroke('#FFFFFF')
    strokeWeight(3)

def draw():
    global y
    background('#004477')
    circle(250, y, 50)
    y += 1
    
