# AUTHOR

__author__ = " Brijesh_krishna                                                                         "
__date__ = " 2020.05.22"
_version_ = " 0.1 "

__package__ = "Baicmath"
__path__ = ""

__file__ = "APV"
__file__path__ = ""
# about
'''
THIS MODULE IS ABOUT AREA,PERIMETER,VOLUME
OR APV  

'''

# importing
import math



def Show_type(value, show_type  ):
    if ((show_type == 0) | (show_type == "r")):
        return value
    elif ((show_type == 1) | (show_type == "p")):
        print(value)







# perimeter

#   #   #   #   #   #   #   #   #   #   #
#   #   #   #   #   #   #   #   #   #   #
#   #   #   #   #   #   #   #   #   #   #


#   #   #   #   #   #   #   #   #   #   #
def perimeter_of_square(side, show_type):
    area = 4 * side
    if ((show_type == 0) | (show_type == "r")):
        return area
    elif ((show_type == 1) | (show_type == "p")):
        print(area)


#   #   #   #   #   #   #   #   #   #   #
def perimeter_of_rectangle(length, width, show_type):
    area = 2 * length + 2 * width
    if ((show_type == 0) | (show_type == "r")):
        return area
    elif ((show_type == 1) | (show_type == "p")):
        print(area)


#   #   #   #   #   #   #   #   #   #   #
def perimeter_of_triangle(side_1, side_2, side_3, show_type):
    area = side_1 + side_2 + side_3
    if ((show_type == 0) | (show_type == "r")):
        return area
    elif ((show_type == 1) | (show_type == "p")):
        print(area)


#   #   #   #   #   #   #   #   #   #   #
def perimeter_of_right_angle_triangle(side_1, side_2, show_type):
    area = side_1 + side_2 + math.sqrt(side_1 ** 2 + side_2 ** 2)
    if ((show_type == 0) | (show_type == "r")):
        return area
    elif ((show_type == 1) | (show_type == "p")):
        print(area)


#   #   #   #   #   #   #   #   #   #   #
def perimeter_of_circle(radius, show_type):
    area = (2 * (22 / 7)) * radius
    if ((show_type == 0) | (show_type == "r")):
        return area
    elif ((show_type == 1) | (show_type == "p")):
        print(area)


def perimeter_of_sector(length_of_the_arc,radius, show_type = 0):
    Show_type((length_of_the_arc + (2*radius)),show_type = show_type)


#   #   #   #   #   #   #   #   #   #   ##   #   #   #   #   #   #   #   #   #   #
#   #   #   #   #   #   #   #   #   #   #
#   #   #   #   #   #   #   #   #   #   #


# area

#   #   #   #   #   #   #   #   #   #   ##   #   #   #   #   #   #   #   #   #   #

#   #   #   #   #   #   #   #   #   #   #
#   #   #   #   #   #   #   #   #   #   #

def area_of_square(side, show_type):
    area = side ** 2
    if ((show_type == 0) | (show_type == "r")):
        return area
    elif ((show_type == 1) | (show_type == "p")):
        print(area)


#   #   #   #   #   #   #   #   #   #   #
def area_of_rectangle(length, width, show_type):
    area = length * width
    if ((show_type == 0) | (show_type == "r")):
        return area
    elif ((show_type == 1) | (show_type == "p")):
        print(area)


#   #   #   #   #   #   #   #   #   #   #
def area_of_triangle_of_two_sides(base, height, show_type):
    area = (1 / 2) * base * height
    if ((show_type == 0) | (show_type == "r")):
        return area
    elif ((show_type == 1) | (show_type == "p")):
        print(area)


#   #   #   #   #   #   #   #   #   #   #
def area_of_triangle_of_three_side(side_1, side_2, side_3, show_type):
    s = (side_2 + side_1 + side_3) / 2
    area = math.sqrt(s * (s - side_1) * (s - side_2) * (s - side_3))
    if ((show_type == 0) | (show_type == "r")):
        return area
    elif ((show_type == 1) | (show_type == "p")):
        print(area)


#   #   #   #   #   #   #   #   #   #   #
def area_of_trapezoid(length_1, length_2, height, show_type):
    area = (length_1 + length_2 / 2) * height
    if ((show_type == 0) | (show_type == "r")):
        return area
    elif ((show_type == 1) | (show_type == "p")):
        print(area)


#   #   #   #   #   #   #   #   #   #   #
def area_of_parallelogram(base, height, show_type):
    area = base * height
    if ((show_type == 0) | (show_type == "r")):
        return area
    elif ((show_type == 1) | (show_type == "p")):
        print(area)


#   #   #   #   #   #   #   #   #   #   #
def area_of_circle(radius, show_type):
    area = (22 / 7) * ((radius) ** 2)
    if ((show_type == 0) | (show_type == "r")):
        return area
    elif ((show_type == 1) | (show_type == "p")):
        print(area)
def area_of_equilateral_in_altitude(altitude, show_type = 0):
    Show_type((math.pow(altitude,2))/math.sqrt(3),show_type = show_type)

def area_of_equilateral_in_side(side, show_type = 0):
    Show_type(((math.sqrt(3)* (math.pow(side,2))))/4,show_type= show_type)

def area_of_sector(length_of_the_arc,radius ,show_type = 0):
    Show_type(value=(length_of_the_arc*radius)/2,show_type= show_type)




#   #   #   #   #   #   #   #   #   #   ##   #   #   #   #   #   #   #   #   #   #

# volume
#   #   #   #   #   #   #   #   #   #   ##   #   #   #   #   #   #   #   #   #   #
#   #   #   #   #   #   #   #   #   #   #

def volume_of_cube(side, show_type):
    area = side ** 3
    if ((show_type == 0) | (show_type == "r")):
        return area
    elif ((show_type == 1) | (show_type == "p")):
        print(area)


#   #   #   #   #   #   #   #   #   #   #
def volume_of_prism(lenght, width, height, show_type):
    area = lenght * width * height
    if ((show_type == 0) | (show_type == "r")):
        return area
    elif ((show_type == 1) | (show_type == "p")):
        print(area)


#   #   #   #   #   #   #   #   #   #   #
def volume_of_cylinder(radius, lenght, show_type):
    area = area_of_circle(radius, show_type=0) * lenght
    if ((show_type == 0) | (show_type == "r")):
        return area
    elif ((show_type == 1) | (show_type == "p")):
        print(area)


#   #   #   #   #   #   #   #   #   #   #
def volume_of_cone(radius, height, show_type):
    area = area_of_circle(radius, show_type=0) * (1 / 3) * height
    if ((show_type == 0) | (show_type == "r")):
        return area
    elif ((show_type == 1) | (show_type == "p")):
        print(area)


#   #   #   #   #   #   #   #   #   #   #
def volume_of_sphere(radius, show_type):
    area = (22 / 7) * (radius ** 3) * (4 / 3)
    if ((show_type == 0) | (show_type == "r")):
        return area
    elif ((show_type == 1) | (show_type == "p")):
        print(area)
#   #   #   #   #   #   #   #   #   #   #
#   #   #   #   #   #   #   #   #   #   #
#   #   #   #   #   #   #   #   #   #   #
#   #   #   #   #   #   #   #   #   #   # END #   #   #   #   #   #   #   #   #   #   #

