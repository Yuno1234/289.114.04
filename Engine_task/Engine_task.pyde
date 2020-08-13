theta = 0
r = 20
diameter = r * 2

def setup():
    size(800, 400)
    noFill()
    stroke('#FFFFFF')
    strokeWeight(3)
    
def draw():
    global theta
    background('#004477')
    
    pushMatrix()
    translate(150, 220)
    x = cos(theta)
    y = sin(theta+PI/2)
    line(0, y*r, 0, -55+y*r)
    rect(-15, -75+y*r, 30, 28)
    line(-15, -70+y*r, 15, -70+y*r)
    line(-15, -65+y*r, 15, -65+y*r)
    popMatrix()
    
    pushMatrix()
    translate(200, 220)
    x = cos(theta)
    y = sin(theta-PI/2)
    line(0, y*r, 0, -55+y*r)
    rect(-15, -75+y*r, 30, 28)
    line(-15, -70+y*r, 15, -70+y*r)
    line(-15, -65+y*r, 15, -65+y*r)
    popMatrix()
    
    pushMatrix()
    translate(250, 220)
    x = cos(theta)
    y = sin(theta)
    line(0, y*r, 0, -55+y*r)
    rect(-15, -75+y*r, 30, 28)
    line(-15, -70+y*r, 15, -70+y*r)
    line(-15, -65+y*r, 15, -65+y*r)
    popMatrix()
    
    pushMatrix()
    translate(600, 220)
    circle(0, 0, diameter)
    x = cos(theta)
    y = sin(theta)
    line(x*r, y*r, 0, 0)
    line(x*r, y*r, 0, -55+y*r)
    rect(-15, -75+y*r, 30, 28)
    line(-15, -70+y*r, 15, -70+y*r)
    line(-15, -65+y*r, 15, -65+y*r)
    theta += 0.075
    popMatrix()
    
    
