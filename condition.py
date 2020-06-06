# import
import logicmath


import math
import cmath

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


def Is_prime(number, show_type=0):
    for x in range(2, number):
        if number % x == 0:
            if ((show_type == 0) | (show_type == "r")):
                return False
            elif ((show_type == 1) | (show_type == "p")):
                print("False")
            break
        else:

            if ((show_type == 0) | (show_type == "r")):
                return True
            elif ((show_type == 1) | (show_type == "p")):
                print("True")

            break


def find_prime(number, show_type=0):
    if Is_prime(number):
        if ((show_type == 0) | (show_type == "r")):
            return 1, number
        elif ((show_type == 1) | (show_type == "p")):
            print(1)
            print(number)


    else:
        a = []

        for x in range(1, number + 1):
            if number % x == 0:
                a.append(x)

        if ((show_type == 0) | (show_type == "r")):
            return a
        elif ((show_type == 1) | (show_type == "p")):
            print(a)


def Is_equall(number_1, number_2, show_type=0):
    if number_1 == number_2:
        if ((show_type == 0) | (show_type == "r")):
            return True
        elif ((show_type == 1) | (show_type == "p")):
            print("True")
    elif number_1 != number_2:
        if ((show_type == 0) | (show_type == "r")):
            return False
        elif ((show_type == 1) | (show_type == "p")):
            print("False")


def Is_not_equall(number_1, number_2, show_type=0):
    if Is_equall(number_1, number_2):
        if ((show_type == 0) | (show_type == "r")):
            return False
        elif ((show_type == 1) | (show_type == "p")):
            print("False")
    elif Is_equall(number_1, number_2) == False:
        if ((show_type == 0) | (show_type == "r")):
            return True
        elif ((show_type == 1) | (show_type == "p")):
            print("True")


def Is_added(*number, result, show_type=0):
    def total(*number):
        return sum(number)
    i = 0
    if (Is_equall(sum(number), result) | (i == 0)):
        if ((show_type == 0) | (show_type == "r")):
            return True
        elif ((show_type == 1) | (show_type == "p")):
            print("True")
            i = 1
         
    elif Is_not_equall(total(*number), result):
        if ((show_type == 0) | (show_type == "r")):
            return False
        elif ((show_type == 1) | (show_type == "p")):
            print("False")


#	#	#	#	#	#	#	#	#	#	#


#	#	#	#	#	#	#	#	#	#	#
#	#	#	#	#	#	#	#	#	#	#
#	#	#	#	#	#	#	#	#	#	#

def Show_type(value, show_type):
    if ((show_type == 0) | (show_type == "r")):
        return value
    elif ((show_type == 1) | (show_type == "p")):
        print(value)


#	#	#	#	#	#	#	#	#	#	#
#	#	#	#	#	#	#	#	#	#	#


#	#	#	#	#	#	#	#	#	#	#
#	#	#	#	#	#	#	#	#	#	#

#	#	#	#	#	#	#	#	#	#	#
#	#	#	#	#	#	#	#	#	#	#
#	#	#	#	#	#	#	#	#	#	#




