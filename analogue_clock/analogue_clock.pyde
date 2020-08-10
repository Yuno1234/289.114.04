def setup():
    size(500,500)
    noFill()
    stroke('#FFFFFF')
    
def draw():
    background('#004477')
    translate(width/2, height/2)
    strokeWeight(3)
    circle(0, 0, 350)
    
    rotate(-PI/2)
    
    h = TAU/12 * hour()
    pushMatrix()
    rotate(h)
    strokeWeight(10)
    line(0, 0, 100, 0)
    popMatrix()
    
    m = TAU/60 * minute()
    pushMatrix()
    rotate(m)
    strokeWeight(5)
    line(0, 0, 120, 0)
    popMatrix()
    
    s = TAU/60 * second()
    pushMatrix()
    rotate(s)
    strokeWeight(2)
    line(0, 0, 130, 0)
    popMatrix()
