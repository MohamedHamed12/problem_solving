# https://www.hackerrank.com/challenges/positive-lookahead/problem?isFullScreen=true

Regex_Pattern = r'o(?=oo)'	# Do not delete 'r'.

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))
