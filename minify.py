"""
    Copyright 2016 Dee Reddy

"""
import sys
import re

args = sys.argv[1:]


def minify(filepath, comments=False):
    """ Minifies/uglifies file
    :param
        file_:
        comments: Boolean. If False, deletes comments during output.
    :return:
    """

    output = ''
    with open(filepath, "r") as file_:
        for line in file_:
            temp = ''
            for char in line:
                if (char != ' ') and (char != '\n'):
                    temp += char
            output += temp
    return output


if __name__ == "__main__":
    print(minify('./stylesheet.css'))
