# https://www.hackerrank.com/challenges/matching-digits-non-digit-character/problem?isFullScreen=true

Regex_Pattern = r"\d{2}\D{1}\d{2}\D{1}\d{4}"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
