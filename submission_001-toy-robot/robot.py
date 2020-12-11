def move_square(size):
    '''
    This function is in charge of moving as square.
    '''
    print("Moving in a square of size "+str(size))
    for i in range(4):
        degrees = 90
        print("* Move Forward "+str(size))
        print("* Turn Right "+str(degrees)+" degrees")


def move_rectangle(length, width):
    '''
    The function moves the robot in a rectangle form.
    '''
    print("Moving in a rectangle of "+str(length)+" by "+str(width))
    for i in range(2):
        degrees = 90
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")
        print("* Move Forward "+str(width))
        print("* Turn Right "+str(degrees)+" degrees")


def move_circle():
    '''
    Moves the robot in a circular move.
    '''
    print("Moving in a circle")
    degrees = 1
    length = 1
    for i in range(360):
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")


def dancing_square(length):
    '''
    Moves the robot to dance in a square move.
    '''
    print("Square dancing - 3 squares of size 20")
    for i in range(3):
        print("* Move Forward "+str(length))
        move_square(length)


def crop_circle(length):
    '''
    The robot will move in a cropped circular move.
    '''
    print("Crop circles - 4 circles")
    for i in range(4):
        print("* Move Forward "+str(length))
        move_circle()


def move():
    '''
    Variables are initialised.
    Other functions are called by this function.
    '''
    size = 10
    length = 20
    width = 10
    move_square(size)
    move_rectangle(length, width)
    move_circle()
    dancing_square(length)
    crop_circle(length)


def robot_start():
    '''
    Calls the function responsible to move the robot.
    '''
    move()


if __name__ == "__main__":
    robot_start()
