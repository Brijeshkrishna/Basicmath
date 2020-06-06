import math



def factorial_of(n):
    sum  = n
    while 2<=n :
        sum = sum * (n-1)
        n = n-1
    return sum


def permutation(n,r):
    if n>= r :
        if n == r:
            return 1
        else :
            return factorial_of(n)/factorial_of(n-r)
def ispermutation(n,r):
    if n>=r:
        return True
    else:
        return False

def commbnation(n,r):
    return permutation(n,r)/factorial_of(r)

def iscommbnation(n,r):
    if n>=r:
        return True
    else:
        return False

#log_funtions
def log_of(log_value,show_type = "r"):
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

    if log_value == 0:
        if (show_type == "r")  | (show_type == 0):
            return "infinity"
        elif (show_type == "p") |(show_type == 1)  :
            print ("infinity")
    elif (Is_even(log_value) )| (Is_odd(log_value)):
        if (show_type == "r")  | (show_type == 0):
            return math.log(log_value)
        elif (show_type == "p") |(show_type == 1)  :
            print( math.log(log_value))





def log_to_base(log_value,base,show_type= "r"):
    log_value_ = log_of(log_value)/log_of(base)
    if (show_type == "r") | (show_type == 0) :
        return log_value_
    elif (show_type == "p") | (show_type == 1):
        print(log_value_)
#   #   #   #   #   #   #   #   #   #   #


def total(*number,show_type = 0):
    if ((show_type == 0) | (show_type == "r")):
            return sum(number)
    elif ((show_type == 1) | (show_type == "p")):
            print(sum(number))
#   #   #   #   #   #   #   #   #   #   #
# i want to sub as same as above


#   #   #   #   #   #   #   #   #   #   #
def divide(numarator,denomenater,show_type = 0):
    result = (numarator/denomenater)
    if ((show_type == 0) | (show_type == "r")):
        return result
    elif ((show_type == 1) | (show_type == "p")):
        print(result)




#   #   #   #   #   #   #   #   #   #   #
#   #   #   #   #   #   #   #   #   #   #
def divide_of_quocent(numarator,denomenator,show_type=0):
    result = numarator % denomenator
    if ((show_type == 0) | (show_type == "r")):
        return result
    elif ((show_type == 1) | (show_type == "p")):
        print(result)

