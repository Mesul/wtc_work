

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    shape = input("Shape?: ")
    lshape = shape.lower()
    while(1):
        if lshape == "pyramid" or lshape == "p":
            return('pyramid')
        elif lshape == "square" or lshape == "s":
            return('square')
        elif lshape == "triangle" or lshape == "t":
            return('triangle')
        else:
            shape = input("Shape?: ")
            lshape = shape.lower()
    


# TODO: Step 1 - get height (it must be int!)
def get_height():
    height = input("Height?: ")

    while(1):
        if height.isdigit():
            return(int(height))
        else:
            height = input("Height?: ")


# TODO: Step 2
def draw_pyramid(height, outline):
    if outline:
        space = 1
        for rows in range(height):
            if rows == 0:
                print(" "*(height-rows-1)+ "*")
            elif rows < height-1:
                print(" "*(height-rows-1)+ "*" + " "*space + "*")
                space += 2
            else:
                print("*"*(height*2-1))
        '''for rows in range(1, height+1):
            for cols in range(1, 2*height):
                if rows == height or (rows+cols) == height +1 or cols-rows == height-1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()'''
    else:
        for i in range(height):
            print(" "*(height-i-1) + "*"*(2*i+1))
    


# TODO: Step 3
def draw_square(height, outline):
    if outline:
        for rows in range(height):
            for cols in range(height):
                if rows == 0 or rows == height-1 or cols == height-1 or cols == 0:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    else:
        for i in range(height):
            print("*" * height)


# TODO: Step 4
def draw_triangle(height, outline):
    if outline:
        space = 0
        for rows in range(height):
            if rows == 0:
                print("*")
            elif rows < height -1:
                print("*" + " " * space + "*")
                space += 1
            else:
                print("*"*height)
        '''for rows in range(height):
            for cols in range(height):
                if cols == rows or cols == 0 or rows == height-1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()'''
    else:
        for i in range(1,height+1):
            print("*"*i)
        


# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape == "pyramid":
        draw_pyramid(height, outline)
    elif shape == "square":
        draw_square(height, outline)
    elif shape == "triangle":
        draw_triangle(height, outline)


# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    outli = input("Outline only? (y/N): ")
    outline = outli.lower()
    while(1):
        if outline == "y":
            return(True)
        elif outline == "n":
            return(False)
        else:
            outli = input("Outline only? (y/N): ")


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

#*\n**\n* *\n*  *\n*****\n
#*\n**\n* *\n*  *\n*   *\n