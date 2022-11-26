def setup():
    # Set the size of your sketch
    size(500,500)

    
def draw():
    # Starting with the largest ellipse, use a for loop to draw a bullseye with ellipses
    for i in range(8):
        ellipse(250, 250, 160 - (i*20), 160 -(i*20))
    # Use an if statement and modulo to alternate the color of your rings
        if(i % 2 == 1):
            fill("#080707")
        else:
            fill("#EA1313")
        
