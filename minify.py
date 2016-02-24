"""
    Minify/uglify CSS files -- i.e. removes spaces and comments from files
    Specify input and output paths in command line arg:
    `$ python minify.py ./src/styles.css ./src/output.css`

    Copyright 2016 Dee Reddy

    TODO:
        -Add JS option (detect file type)
"""
import sys
import re


def minify(input_path, output_path):
    """ Minifies/uglifies file

        Args:
            input_path:     input file path
            output_path:    write-out file path
            comments:       Boolean. If False, deletes comments during output.
        Returns:
            Minified string.
        Example:
            `$ python minify.py ./src/styles.css ./src/output.css`
    """

    # matches all in-line and multi-line comments; matches all spaces:
    pattern = re.compile(r"""
    \s |                    # matches all whitespace characters OR
    (                       # OR any char between /* */ (inclusive)
        /\*
        (.|\n)*?            # N.b. `*?` performs non-greedy match
        \*/
    )
    | //.*\n                # OR any char from // until new-line (inclusive)
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
