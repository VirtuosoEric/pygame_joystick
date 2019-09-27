import pygame

pygame.init()

done = False

pygame.joystick.init()

joystick = pygame.joystick.Joystick(0)
joystick.init()

print joystick.get_name()

axes = joystick.get_numaxes()
print 'axes',axes

buttons = joystick.get_numbuttons()
print 'buttons',buttons

hats = joystick.get_numhats()
print 'hats', hats

balls = joystick.get_numballs()
print 'balls', balls

index = 0


# -------- Main Program Loop -----------
while done==False:
    # EVENT PROCESSING STEP
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            print "You pressed",event.button
        if event.type == pygame.JOYBUTTONUP:
            print "You released",event.button
        if event.type == pygame.JOYBALLMOTION:
            print "ball motion"
        if event.type == pygame.JOYAXISMOTION:
            print "axies motion",event.axis, event.value
        if event.type == pygame.JOYHATMOTION:
            print "hat motion"

        
        
        for i in range( axes ):
            axis = joystick.get_axis( i )

        for i in range( buttons ):
            button = joystick.get_button( i )

        for i in range( hats ):
            hat = joystick.get_hat( i )

        for i in range( balls ):
            ball = joystick.get_ball(i)

pygame.quit ()
        
        