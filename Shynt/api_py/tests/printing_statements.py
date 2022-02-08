
"""
    About printing sumbols and colors with unicode syntax:
    - https://stackoverflow.com/questions/38760554/how-to-print-cross-mark-or-check-mark-in-tcl
    - https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal


    At the moment nose will be used with unittest, for UX improvement
    see customization to use the following functions
"""


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'





def test_did_passed(test_type):
    s = f"\n{bcolors.OKGREEN} Testing of {test_type} passed: "
    s += '\u2714'
    s += bcolors.ENDC
    return s


def test_did_not_passed(test_type):
    s = f"\n{bcolors.FAIL} Testing of {test_type} did not passed: "
    s += '\u2718'
    return s