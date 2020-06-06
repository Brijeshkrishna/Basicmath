# import

import math


# funtion
def Show_type(value, show_type  ):
    if ((show_type == 0) | (show_type == "r")):
        return value
    elif ((show_type == 1) | (show_type == "p")):
        print(value)




#	#	#	#	#	#	#	#	#	#	#
def sin(value_in_degree, show_type=None):  # sine
    if show_type == None:
        return math.sin(value_in_degree)
    elif show_type == "p":
        print(math.sin(value_in_degree))


#	#	#	#	#	#	#	#	#	#	#
def cos(value_in_degree, show_type=None):
    if show_type == None:
        return math.cos(value_in_degree)
    elif show_type == "p":
        print(math.cos(value_in_degree))


#	#	#	#	#	#	#	#	#	#	#
def tan(value_in_degree, show_type=None):
    if show_type == None:
        return math.tan(value_in_degree)
    elif show_type == "p":
        print(math.tan(value_in_degree))


#	#	#	#	#	#	#	#	#	#	#
def sin_invers(value_in_degree, show_type=None):
    if show_type == None:
        return math.asin(value_in_degree)
    elif show_type == "p":
        print(math.asin(value_in_degree))


#	#	#	#	#	#	#	#	#	#	#
def cos_invers(value_in_degree, show_type=None):
    if show_type == None:
        return math.acos(value_in_degree)
    elif show_type == "p":
        print(math.acos(value_in_degree))


#	#	#	#	#	#	#	#	#	#	#
def tan_invers(value_in_degree, show_type=None):
    if show_type == None:
        return math.atan(value_in_degree)
    elif show_type == "p":
        print(math.atan(value_in_degree))


#	#	#	#	#	#	#	#	#	#	#
def cosec(value_in_degree, show_type=None):
    if show_type == None:
        return 1/(math.sin(value_in_degree))
    elif show_type == "p":
        print(1/(math.sin(value_in_degree)))


#	#	#	#	#	#	#	#	#	#	#
def sec(value_in_degree, show_type=None):
    if show_type == None:
        return 1/(math.cos(value_in_degree))
    elif show_type == "p":
        print(1/(math.cos(value_in_degree)))


#	#	#	#	#	#	#	#	#	#	#
def cot(value_in_degree, show_type=None):
    if show_type == None:
        return 1/(math.tan(value_in_degree))
    elif show_type == "p":
        print(1/(math.tan(value_in_degree)))


#	#	#	#	#	#	#	#	#	#	#
def cosec_invers(value_in_degree, show_type=None):
    Show_type(float(1/sin_invers(value_in_degree = value_in_degree)),show_type = show_type)

#	#	#	#	#	#	#	#	#	#	#
def sec_invers(value_in_degree, show_type=0):
    Show_type(float(1 / cos_invers(value_in_degree=value_in_degree)), show_type=show_type)

#	#	#	#	#	#	#	#	#	#	#
def cot_invers(value_in_degree, show_type=None):
    Show_type(float(1 / tan_invers(value_in_degree=value_in_degree)), show_type=show_type)



#	#	#	#	#	#	#	#	#	#	#
def is_right_angle_triangle(side1, side2, side3, show_type="r"):
    if (math.pow(side1, 2) == math.pow(side2, 2) + math.pow(side3, 2)) | (
            math.pow(side3, 2) == math.pow(side2, 2) + math.pow(side1, 2)) | (
            math.pow(side2, 2) == math.pow(side3, 2) + math.pow(side1, 2)):
        right_angle_triangle = True

    else:
        right_angle_triangle = False
    if (show_type == "p") | (show_type == 1):
        print(right_angle_triangle)
    elif (show_type == "r") | (show_type == 0):
        return right_angle_triangle


#	#	#	#	#	#	#	#	#	#	#
def find_two_sides_of_triangle(side1, show_type="r"):
    def Is_even(number, show_type="r"):
        if number % 2 == 0:
            number_is = True
        else:
            number_is = False
        if (show_type == "r") | (show_type == 0):
            return number_is
        elif (show_type == "p") | (show_type == 1):
            print(number_is)

    def Is_odd(number, show_type="r"):
        if number % 2 != 0:
            number_is = True
        else:
            number_is = False
        if (show_type == "r") | (show_type == 0):
            return number_is
        elif (show_type == "p") | (show_type == 1):
            print(number_is)

    if (side1 == 0):
        if (show_type == "p") | (show_type == 1):
            print("0")
            print("0")
        elif (show_type == "r") | (show_type == 0):
            return 0, 0

    else:
        def Is_even(number, show_type="r"):
            if number % 2 == 0:
                number_is = True
            else:
                number_is = False
            if (show_type == "r") | (show_type == 0):
                return number_is
            elif (show_type == "p") | (show_type == 1):
                print(number_is)

        def Is_odd(number, show_type="r"):
            if number % 2 != 0:
                number_is = True
            else:
                number_is = False
            if (show_type == "r") | (show_type == 0):
                return number_is
            elif (show_type == "p") | (show_type == 1):
                print(number_is)

        if Is_even(side1):
            side = (side1 / 2) ** 2
            side2_even = side + 1
            side3_even = side - 1
            if (show_type == "p") | (show_type == 1):
                print(side2_even)
                print(side3_even)
            elif (show_type == "r") | (show_type == 0):
                return side2_even, side3_even

        elif Is_odd(side1):
            side2_odd = ((side1 - 1) / 2) ** 2
            side3_odd = side2_odd - 1

            if (show_type == "p") | (show_type == 1):
                print(side2_odd)
                print(side3_odd)
            elif ((show_type == "r") | (show_type == 0)):
                return side2_odd, side3_odd
#	#	#	#	#	#	#	#	#	#	#


