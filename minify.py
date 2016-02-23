"""
    Copyright 2016 Dee Reddy

"""
import sys
import re

args = sys.argv[1:]


def minify(input_path, output_path, comments=False):
    """ Minifies/uglifies file
    args:
        input_path: input file path
        output_path: write-out file path
        comments: Boolean. If False, deletes comments during output.
    returns:
        Minified string.
    example:
        `$ python minify.py ./src/styles.css ./src/output.css`
    """

    pattern = re.compile(r"""
    \s |                                # matches all whitespace characters OR
     (                                  #
        /\*                             # /* AND
        [                               # 0 or more of any character
            \w\s                        #
            (?=\*)                      # (positive lookahead: doesn't make * part of the match)
            :@!"'~,#%&-=;<>`            #
            \.\^\$\+\{\[\]\\\|          #
        ]*                              #
        \*/                             # AND */
     )                                  #
     | //.*\n                           # OR any character from // until end-line (inclusive)
    """, re.VERBOSE)

    # read file and apply regex:
    with open(input_path, "r") as file_in:
        temp = []
        for line in file_in:
            temp.append(line)
        output = ''.join(temp)
        output = pattern.sub('', output)

    # write to file:
    # (`w+` mode: writing/reading; overwrites existing files; creates file if doesn't exit)
    with open(output_path, "w+") as file_out:
        file_out.write(output)

#############################
#           Main            #
#############################
if __name__ == "__main__":
    # specify input and output paths in args:
    minify(args[0], args[1])
