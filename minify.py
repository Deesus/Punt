"""
    Minify/uglify CSS files -- i.e. removes spaces and comments from files
    S
    pecify input and output paths in command line arg:
    `$ python minify.py ./src/styles.css ./src/output.css`

    TODO:
        -Add JS option (detect file type)
"""
__author__ = ('Dee Reddy', "deesus@yandex.com")

import sys
import re


def minify(input_path, output_path):
    """ Minifies/uglifies file

        Args:
            input_path:     Input file path.
            output_path:    Write-out file path.
        Returns:
            Minified string.
        Example:
            `$ python minify.py ./src/styles.css ./src/output.css`
    """

    # matches all in-line comments `//`,  multi-line comments `/**/`; matches all spaces:
    pattern = re.compile(r"""
    # Match comments:
    (                           # any char between `/* */` (inclusive)
        /\*
        (.|\n)*?                # (N.b. `*?` performs non-greedy match)
        \*/
    )
    | //.*\n                    # OR any char from `//` until new-line (inclusive)

    # Match spaces:
    | \s+(?=[^{]*})             # OR all space characters inside `{ }`
    | \s(?={)                   # OR a whitespace before `{`
    | \ {2,}                    # OR multiple space chars
    | [\t\n\r\f\v]              # OR tab, linefeed, carriage return, form feed, vertical tab -- N.b.
                                # we exclude `\ ` to preserve spaces between child selectors)
    """, re.VERBOSE)

    # read file and apply regex:
    with open(input_path, "r") as file_in:
        output = [line for line in file_in]
        output = ''.join(output)
        output = pattern.sub('', output)

    # write to file:
    # (`w+` mode: writing/reading; overwrites existing files; creates file if doesn't exit)
    with open(output_path, "w+") as file_out:
        file_out.write(output)

######################################
#                 Main               #
######################################
if __name__ == "__main__":
    args = sys.argv[1:]
    minify(args[0], args[1])
