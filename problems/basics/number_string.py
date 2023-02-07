def number_string(x):
    """
    Given a number x, produce a string: "POSITIVE", "NEGATIVE", "ZERO"
    (depending on whether the number is positive, negative, or zero)
    """

    if x > 0:
        result = "POSITIVE"
    elif x < 0:
        result = "NEGATIVE"
    else:
        result = "ZERO"
    s = None

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return result


#############################################################
###                                                       ###
###                    Testing code.                      ###
###    !!! DO NOT MODIFY ANY CODE BELOW THIS POINT !!!    ###
###                                                       ###
#############################################################

import sys
sys.path.append('../')

import test_utils as utils

def do_test_number_string(x, expected):
    recreate_msg = utils.gen_recreate_msg("number_string", *(x,))

    actual = number_string(x)

    utils.check_none(actual, recreate_msg)
    utils.check_type(actual, expected, recreate_msg)
    utils.check_equals(actual, expected, recreate_msg)


def test_number_string_1():
    do_test_number_string(x=10, expected="POSITIVE")


def test_number_string_2():
    do_test_number_string(x=-7, expected="NEGATIVE")


def test_number_string_3():
    do_test_number_string(x=0, expected="ZERO")