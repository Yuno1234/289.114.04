theta = 0
r = 100
diameter = r * 2

def setup():
    size(600,600)
    noFill()
    stroke('#FFFFFF')
    strokeWeight(3)
    
def draw():
    global theta
    background('#004477')
    translate(width/2, height/2)
    circle(0, 0, diameter)
    x = cos(theta)
    y = sin(theta)
    circle(x*r, y*r, 5)
    theta += 0.05
    
    
