import sys, re
"""
    Prettify/clean up CSS files -- i.e. adds proper spacing and newlines.
    Specify input and output paths in command line arg -- optionally specify tab amount:
    `$ python prettify.py ./src/styles.css ./src/output.css 4`
"""
__author__ = ('Dee Reddy', 'deesus@yandex.com')


def prettify(input_path, output_path, tab_length=4):
    """ Prettifies/cleans CSS file

        Args:
            input_path:     (str) Input file path.
            output_path:    (str) Write-out file path.
            tab_length:     (int) Number of spaces when tabbing line. Defaults to 4.
        Returns:
            Writes prettified file.
        Example:
            `$ python prettify.py ./src/styles.css ./src/output.css 2`
    """

    # check for options (e.g. tab length):
    if len(sys.argv) > 3:
        try:
            tab_length = int(sys.argv[3])
        except:
            print("Invalid argument for tab length: must be int.")
            print("Using default tab spaces (4) instead.")

    # space char replacements:
    space_regex = re.compile(r"""
    \s+(?=[^{]*})           # OR all space characters inside `{ }`
    | \s(?={)               # OR a whitespace before `{`
    | \ {2,}                # OR multiple space chars
    | [\t\n\r\f\v]          # OR tab, linefeed, carriage return, form feed, vertical tab -- N.b.
                            # we exclude `\ ` to preserve spaces between child selectors)
    """, re.VERBOSE)

    # newline replacements:
    newline_regex = re.compile(r"""
    (?<=[{}])               # Look behind for `{` or `}`
    | (?<=;)                # OR look behind for `;`
    """, re.VERBOSE)

    # tab replacements:
    tab_regex = re.compile(r"""
    \n+(?!})(?=[^{]*})      # all newline chars inside `{ }` except last instance (i.e. don't match `\n}`)
    """, re.VERBOSE)

    # read file and apply regex:
    with open(input_path, "r") as file_:
        output = [line for line in file_]
        output = ''.join(output)
        # apply regexes:
        output = space_regex.sub('', output)
        output = newline_regex.sub('\n', output)
        output = tab_regex.sub('\n' + (' ' * tab_length), output)

    # write to file:
    # (`w+` mode: writing/reading; overwrites existing files; creates file if doesn't exit)
    with open(output_path, "w+") as file_out:
        file_out.write(output)
        print("*** file successfully written ***")


######################################
#                 Main               #
######################################
if __name__ == "__main__":
    prettify(sys.argv[1], sys.argv[2])
