import turtle


def draw_side(flag_width, flag_height):
    
    turtle.forward(flag_height) 
    turtle.right(90)
    turtle.forward(flag_width)
    turtle.right(90)
    turtle.forward(flag_height)
    turtle.right(90)
    turtle.forward(flag_width)
    turtle.right(90)

def draw_rectangle(x, y, flag_width, flag_height, color, outline_color):
   
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.pencolor(outline_color)
    turtle.pensize(2)
    turtle.fillcolor(color)
    turtle.begin_fill()
    draw_side(flag_width, flag_height)
    turtle.end_fill()

def draw_circle(x, y, radius, color, outline_color):

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.pencolor(outline_color)
    turtle.pensize(1)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()




def draw_flagpole(x, y, flag_height, color):

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.pensize(3)
    turtle.setheading(90)
    turtle.forward(flag_height * 3)


def draw_flag(x, y, scale_factor):
 
    flag_width = 150 * scale_factor
    flag_height = 100 * scale_factor
    flagpole_height = flag_height


    draw_flagpole(x, y, flagpole_height, "black")

    flag_x = x + 10
    flag_y = y + flagpole_height * 2

    draw_rectangle(flag_x, flag_y, flag_width, flag_height, "red", "red")

  
    circle_radius = 20 * scale_factor
    circle_x = 6
    circle_y = 100

    

    draw_circle(circle_x, circle_y, circle_radius, "white", "white")

def draw_flag2(x, y, scale_factor):
 
    flag_width = 150 * scale_factor
    flag_height = 100 * scale_factor
    flagpole_height = flag_height


    draw_flagpole(x, y, flagpole_height, "black")

    flag_x = x + 10
    flag_y = y + flagpole_height * 2

    draw_rectangle(flag_x, flag_y, flag_width, flag_height, "red", "red")

  
    circle_radius = 20 * scale_factor
    circle_x = 276 
    circle_y = 25
    

    draw_circle(circle_x, circle_y, circle_radius, "white", "white")


    
# Main function
def main():
 
    turtle.setup(800, 600)
    turtle.bgcolor("lightblue")  


    draw_flag(-100, -150, 1.0) 
    draw_flag2(200, -150, 0.7) 


    turtle.done()


main()
