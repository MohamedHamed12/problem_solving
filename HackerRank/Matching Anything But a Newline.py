# https://www.hackerrank.com/challenges/matching-anything-but-new-line/problem?isFullScreen=true
regex_pattern = r"^.{3}\..{3}\..{3}\..{3}$"	# Do not delete 'r'.

import re
import sys

test_string = input()

match = re.match(regex_pattern, test_string) is not None

print(str(match).lower())
