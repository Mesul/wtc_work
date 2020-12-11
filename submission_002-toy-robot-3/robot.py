"""
TODO: You can either work from this skeleton, or you can build on your solution for Toy Robot 2 exercise.
"""


# list of valid command names allowed
valid_commands = ['off', 'help', 'forward', 'back', 'right', 'left', 'sprint', 'replay']
replay_commands = ['silent', 'reversed', 'reversed silent']

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit variables
min_y, max_y = -200, 200
min_x, max_x = -100, 100

# history list
history = []

# flags
silent = False


def get_robot_name():
    '''
    Responsible to prompt user to name the robot.
    '''
    name = input("What do you want to name your robot? ").strip()
    while len(name) == 0:
        name = input("What do you want to name your robot? ")
    return name


def get_command(robot_name):
    """
    Takes command from user to robot.
    Checks length of command if valid.
    Also validates the command if is it acceptable or not.
    """
    global silent

    in_prom = ''+robot_name+': What must I do next? '
    command = input(in_prom).strip()

    if 'silent' in command.lower():
            silent = True

    range_valid = check_replay_range(command.lower())

    if len(command) == 0 or not valid_command(command.lower()) or not range_valid:
        output(robot_name, "Sorry, I did not understand '"+command+"'.")
        command = input(in_prom)

    if 'replay' not in command.lower():
        history_commands = do_history(command.lower())
    
    return command.lower()


def check_replay_range(command):
    '''
    Checks if replay input is acceptable or not and within allowed range.
    Handles hyphen.
    '''
    command = command.split()
    hyphen_counter = 0
    has_alpha = False

    for item in command:
        if '-' in item:
            hyphen_counter = item.count('-')
            has_alpha = any(char.isalpha() for char in item)
    
    return False if hyphen_counter > 1 or has_alpha else True
    

def split_command_input(command):
    """
    Responsible of splitting command where there's a space.
    If not a single string, returns the args respectively.
    """
    args = command.split(' ', 1)
    if len(args) > 1:
        return args[0], args[1]
    return args[0], ''


def do_history(command):
    '''
    Appends command to history list.
    '''
    global history
    history.append(command)
    return history


def is_int(value):
    """
    Tests if the string value is an int or not
    :param value: a string value to test
    :return: True if it is an int
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def contains_int(value):
    '''
    Checks if ant int is present.
    '''
    return any(map(str.isdigit, value))


def valid_command(command):
    """
    Returns a boolean indicating if the robot can understand the command or not
    Also checks if there is an argument to the command, and if it a valid int
    """
    global replay_commands

    (command_name, arg1) = split_command_input(command)

    valid_command = command_name.lower() in valid_commands
    arg1_valid = len(arg1) == 0 or is_int(arg1) 
    arg1_valid_2 = arg1 in replay_commands or contains_int(arg1)
    

    return valid_command and ((arg1_valid) or arg1_valid_2)


def output(name, message):
    print(''+name+": "+message)


def do_help():
    """
    Provides help information to the user
    :return: (True, help text) to indicate robot can continue after this command was handled
    """
    return True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
"""


def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        return True
    return False


def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    if update_position(steps):
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """

    if update_position(-steps):
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index

    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0

    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index

    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3

    return True, ' > '+robot_name+' turned left.'


def do_sprint(robot_name, steps):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """

    if steps == 1:
        return do_forward(robot_name, 1)
    else:
        (do_next, command_output) = do_forward(robot_name, steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)


def get_limit_range(command):
    for item in command:
        if contains_int(item):
            return True, item
    return False, ''


def do_replay_limit(command, temp_history):
    global history

    has_int, limit_range = get_limit_range(command)

    if has_int:
        num_replay = limit_range.split('-')
        if len(num_replay) > 1:
            return temp_history[-int(num_replay[0]): -int(num_replay[1])]
        elif len(num_replay) == 1:
            return temp_history[-int(num_replay[0]):]
    else:
        return temp_history


def do_replay(robot_name, command):
    '''
    Responsible of doing the replay of previous commands.
    Does it straight or in reverse.
    '''
    global history, silent

    movement_commands = ['forward', 'back', 'left', 'right', 'sprint']
    replay_counter = 0
    
    command = command.split()
    
    if 'reversed' in command:
        temp_history = history[::-1]
    else:
        temp_history = history

    #added temp_history variable to preserve the original history list    
    temp_history = do_replay_limit(command, temp_history)

    if 'reversed' in command and 'silent' in command:
        # temp_history = temp_history[::-1]
        for item in temp_history:
            if item.split()[0] in movement_commands:
                handle_command(robot_name, item)
                replay_counter += 1
        return True, f" > {robot_name} replayed {replay_counter} commands in reverse silently."
    elif 'reversed' in command:
        # temp_history = temp_history[::-1]
        for item in temp_history:
            if item.split()[0] in movement_commands:
                handle_command(robot_name, item)
                replay_counter += 1
        return True, f" > {robot_name} replayed {replay_counter} commands in reverse."
    elif 'silent' in command:
        for item in temp_history:
            if item.split()[0] in movement_commands:
                handle_command(robot_name, item)
                replay_counter += 1
        return True, f" > {robot_name} replayed {replay_counter} commands silently."
    else:
        for item in temp_history:
            if item.split()[0] in movement_commands:
                handle_command(robot_name, item)
                replay_counter += 1
        return True, f" > {robot_name} replayed {replay_counter} commands."


def handle_command(robot_name, command):
    """
    Handles a command by asking different functions to handle each command.
    :param robot_name: the name given to robot
    :param command: the command entered by user
    :return: `True` if the robot must continue after the command, or else `False` if robot must shutdown
    """
    global silent

    (command_name, arg) = split_command_input(command)

    if command_name == 'off':
        global_reset()
        return False
    elif command_name == 'help':
        (do_next, command_output) = do_help()
    elif command_name == 'forward':
        (do_next, command_output) = do_forward(robot_name, int(arg))
    elif command_name == 'back':
        (do_next, command_output) = do_back(robot_name, int(arg))
    elif command_name == 'right':
        (do_next, command_output) = do_right_turn(robot_name)
    elif command_name == 'left':
        (do_next, command_output) = do_left_turn(robot_name)
    elif command_name == 'sprint':
        (do_next, command_output) = do_sprint(robot_name, int(arg))
    elif 'replay' in command:
        (do_next, command_output) = do_replay(robot_name, command)
        silent = False
    
    if not silent:
        print(command_output)
        show_position(robot_name)
    
    return do_next


def global_reset():
    global position_x, position_y, current_direction_index, history, silent
    
    position_x = 0
    position_y = 0
    current_direction_index = 0
    history = []
    silent = False


def robot_start():
    """This is the entry point for starting my robot"""

    global position_x, position_y, current_direction_index, history

    robot_name = get_robot_name()
    output(robot_name, "Hello kiddo!")

    position_x = 0
    position_y = 0
    current_direction_index = 0

    command = get_command(robot_name)
    while handle_command(robot_name, command):
        command = get_command(robot_name)

    history = []
    output(robot_name, "Shutting down..")


if __name__ == "__main__":
    '''
    Main function that calls the function to start the robot.
    '''
    robot_start()