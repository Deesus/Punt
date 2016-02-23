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

    pattern = re.compile(r"""
        \s |                    # matches all whitespace characters OR
         (                      #
            /\*                 # /*
            [
                \w\s
                (?=\*)
                :@!"'~\.\^\$\+\?\{\}\[\]\\\|\(\)
            ]*                  # AND
            \*/                 # */
         )                      #
         | //.*\n               # OR any character from // until end-line (inclusive)
    """, re.VERBOSE)

    with open(filepath, "r") as file_:
        temp = []
        for line in file_:
            temp.append(line)
        output = ''.join(temp)
        return pattern.sub('', output)


if __name__ == "__main__":
    print(minify('./test/stylesheet.css'))
