x = 0
y = 0
position = 0
commands_list = ['off', 'help', 'forward', 'back', 'right', 'left', 'sprint']

def robot_name():
    '''
    Prompts user to name robot.
    Takes input for the robot's name.
    '''
    my_name = input("What do you want to name your robot? ")
    print(my_name + ": Hello kiddo!")
    return my_name

def robot_commands(my_name, command):
    '''
    Function gets a command as input from the user.
    Validates if command is understood and/or valid.
    Controls the robot's movements.
    '''
    global commands_list, position, x, y
    #command = get_command(my_name)
    commands = command.split()
    
    if command == "off":
        print(f"{my_name}: Shutting down..")
        position = 0
        x = 0
        y = 0
        return True
    elif command == "help":
        help_command()
    elif "forward" in command:
        steps = int(commands[1])
        forward_command(steps, my_name)
    elif "back" in command:
        steps = int(commands[1])
        back_command(steps, my_name)
    elif "right" in command:
        right_command(commands, my_name)
    elif "left" in command:
        left_command(commands, my_name)
    elif "sprint" in command:
        steps = int(commands[1])
        sprint_command(steps, my_name)    
    return False


def get_command(my_name):
    global commands_list

    command = input(f"{my_name}: What must I do next? ").strip()
    #input(f"{my_name}: What must I do next? ").strip() as command

    if command.split()[0].lower() in commands_list:
        return command.lower()        
    else:
        print(f"{my_name}: Sorry, I did not understand '{command}'.")
        return ""


def help_command():
    '''
    Function outputs information about the available commands.
    '''
    print('''I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands''')
#  FORWARD - Robot moved forward
#  BACK - Robot moved back
#  RIGHT - Robot turned right
#  LEFT - Robot turned left
#  SPRINT - Gives robot a short burst of speed and some extra distance'''
#  )


def forward_command(steps, my_name):
    '''
    Checks if the commanded movement is within the boundaries.
    Calls movement function.
    '''
    global x
    global y
    global position

    if (position == 0) and (y+steps <= 200):
        y += steps
        front_movement(my_name, steps)
    elif (position == 1) and (x+steps <= 100):
        x += steps
        front_movement(my_name, steps)
    elif (position == 2) and (y-steps >= -200):
        y -= steps
        front_movement(my_name, steps)
    elif (position == 3) and (x-steps >= -100):
        x -= steps
        front_movement(my_name, steps)
    else:
        reached_limit(my_name)
    return x, y


def back_command(steps, my_name):
    '''
    Checks if the commanded movement is within the boundaries.
    Calls movement function.
    '''
    global x
    global y
    global position

    if (position == 0) and (y-steps >= -200):
        y -= steps
        back_movement(my_name, steps)
    elif (position == 1) and (x-steps >= -100):
        x -= steps
        back_movement(my_name, steps)
    elif (position == 2) and (y+steps <= 200):
        y += steps
        back_movement(my_name, steps)
    elif (position == 3) and (x+steps <= 100):
        x += steps
        back_movement(my_name, steps)
    else:
        reached_limit(my_name)
    return x, y


def front_movement(my_name, steps):
    '''
    Moves robot forward and gives user current coordinates.
    '''
    global x
    global y
    print(f" > {my_name} moved forward by {steps} steps.")
    print(f" > {my_name} now at position ({x},{y}).")
    return x, y


def back_movement(my_name, steps):
    '''
    Moves robot backwards and gives user current coordinates.
    '''
    global x
    global y
    print(f" > {my_name} moved back by {steps} steps.")
    print(f" > {my_name} now at position ({x},{y}).")
    return x, y


def right_command(commands, my_name):
    '''
    Turns robot to face its right hand side from current position.
    After turnining, increments position value.
    If position value is -1, changes it to the value 3.
    Gives user current coordinates.
    '''
    global x
    global y
    global position
    position += 1
    if position == 4:
        position = 0
    print(f" > {my_name} turned right.")
    print(f" > {my_name} now at position ({x},{y}).")
    return x, y


def left_command(commands, my_name):
    '''
    Turns robot to face its left hand side from current position.
    After turnining, decrements position value.
    If position value is -1, changes it to the value 3.
    Gives user current coordinates.
    '''
    global x
    global y
    global position
    position -= 1
    if position == -1:
        position = 3
    print(f" > {my_name} turned left.")
    print(f" > {my_name} now at position ({x},{y}).")
    return x, y


def sprint_command(steps, my_name):
    '''
    Moves robot forward the number of steps indicated.
    Iteratively moves robot forward one less step than the previous forward.
    Moves the robot using recursive approach.
    '''
    global x
    global y
    global position
    if (position == 0) and (steps+y <= 200):
        if steps == 0:
            print(f" > {my_name} now at position ({x},{y}).")
            return steps
        y += steps
        if(steps > 0):
            print(f" > {my_name} moved forward by {steps} steps.")
            sprint_command(steps - 1, my_name)
    elif (position == 1) and (steps+x <= 100):
        if steps == 0:
            print(f" > {my_name} now at position ({x},{y}).")
            return steps
        x += steps
        if(steps > 0):
            print(f" > {my_name} moved forward by {steps} steps.")
            sprint_command(steps - 1, my_name)
    elif (position == 2) and (y-steps >= -200):
        if steps == 0:
            print(f" > {my_name} now at position ({x},{y}).")
            return steps
        y -= steps
        if(steps > 0):
            print(f" > {my_name} moved forward by {steps} steps.")
            sprint_command(steps - 1, my_name)
    elif (position == 3) and (x-steps >= -100):
        if steps == 0:
            print(f" > {my_name} now at position ({x},{y}).")
            return steps
        x -= steps
        if(steps > 0):
            print(f" > {my_name} moved forward by {steps} steps.")
            sprint_command(steps - 1, my_name)
    else:
        reached_limit(my_name)
    return x, y


def reached_limit(my_name):
    '''
    Tells user cannot leave boundary and current coordinates.
    '''
    global x
    global y
    print(f"{my_name}: Sorry, I cannot go outside my safe zone.")
    print(f" > {my_name} now at position ({x},{y}).")
    return x, y


def robot_start():
    """This is the entry function, do not change"""
    '''
    This function calls other functions to control the robot.
    '''
    my_name = robot_name()
    
    off = False
    while not off:
        command = get_command(my_name)
        if command:
            off = robot_commands(my_name, command)


if __name__ == "__main__":
    '''
    Main function that calls the robot to start function.
    '''
    robot_start()
