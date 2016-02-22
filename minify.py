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
        Minified string.
    """

    output = ''
    with open(filepath, "r") as file_:
        output = ''.join(
                    ''.join(
                        char for char in line
                        if (char != ' ') and (char != '\n')
                    )
                    for line in file_)
    return output

line = '''{
    margin: 0; padding: 0;
}
    html { box-sizing: border-box;
}
    *, *::before, *::after { box-sizing: inherit;
}
img {
    /*image automatically resizes to max-width of the boundary*/
'''


if __name__ == "__main__":
    print(minify('./test/stylesheet.css'))
