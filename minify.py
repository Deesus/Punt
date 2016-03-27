import sys, re
"""
    Minify/uglify CSS files -- i.e. removes spaces and comments from files
    Specify input and output paths in command line arg:
    `$ python minify.py ./src/styles.css ./src/output.css`
"""
__author__ = ('Dee Reddy', 'deesus@yandex.com')


def minify(input_path, output_path):
    """ Minifies/uglifies file

        Args:
            input_path:     (str) Input file path.
            output_path:    (str) Write-out file path.
        Returns:
            Writes Minified file.
        Example:
            `$ python minify.py ./src/styles.css ./src/output.css`
    """

    # matches all in-line comments, multi-line comments, and all spaces:
    pattern = re.compile(r"""
    # Match comments:
    (/\*(.|\n)*?\*/)    # Any char between `/* */` (inclusive) -- N.b.
                        #   `*?` performs non-greedy match
    | //.*\n            # OR any char from `//` until new-line (inclusive)

    # Match spaces:
    | \s+(?=[^{]*})     # OR all space chars inside `{ }` (assumes no dangling or nested braces)
    | \s(?={)           # OR a whitespace before `{`
    | \ {2,}            # OR multiple space chars
    | [\t\n\r\f\v]      # OR tab, linefeed, carriage return, form feed, vertical tab -- N.b.
                        #   we exclude `\ ` to preserve spaces between child selectors)
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
    minify(sys.argv[1], sys.argv[2])
