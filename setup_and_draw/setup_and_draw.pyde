def setup():
    frameRate(5)
    size(500, 500)
    background('#004477')
    noFill()
    stroke('#FFFFFF')
    strokeWeight(3)
    
def draw():
    background('#004477')
    if frameCount % 2 == 0:
        circle(250, 140, 47)
