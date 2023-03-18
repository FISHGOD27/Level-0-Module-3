def setup():
    size(500,500)
    global y
    global x
    global y2
    global x2
    y2=random(50,450)
    x2=random(50,450)
    y=250
    x=250
def draw():
    noStroke()
    global y
    global x
    fill("#082AFF")
    ellipse(x,y,30,30)
    if keyCode==UP:
        y-=5
    if keyCode==DOWN:
        y+=5
    if keyCode==RIGHT:
        x+=5
    if keyCode==LEFT:
        x-=5
