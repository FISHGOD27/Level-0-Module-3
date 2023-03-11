color = '#FFFFFF'

def setup():

    size(500, 500)
    global x
    global y
    global x2
    global y2
    global counter
    global speed
    global running
    running = True
    counter = 0
    x = 250
    y = 250
    x2 = random(30, 270)
    y2 = -300
    fill("#0343FC")

def draw():
    global color
    background(color)
    global x
    global y
    global x2
    global y2
    global counter
    global e
    global running
    textSize(15)
    e = text(counter, width/11, height/3)
    fill('#FF0D0D')
    rect(x2, y2, 100, 200)
    fill('#0052FF')
    ellipse(x, y, 50, 50)
    if keyCode == RIGHT:
        x+=5
        y2+=5
    elif keyCode == LEFT:
        x-=5
        y2+=5
    if y2 >= height and running:
        y2=0
        x2 = random(0, width)
        counter+=1
    elif x <= x2+50 and x >= x2-50 and y <= y2+200 and y >=y2-200:
        x=50000
        y2=50000
        running =False
