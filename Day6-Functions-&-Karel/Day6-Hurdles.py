#Karel The Robot Project

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    move()
    while wall_on_right():
        if front_is_clear():
            move()
        else:
            break
    turn_left()
  
while not at_goal():
    if front_is_clear():
        move()
    else:
        jump( )
   
    
    
