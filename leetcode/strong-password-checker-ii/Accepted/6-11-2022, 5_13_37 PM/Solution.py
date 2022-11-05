// https://leetcode.com/problems/strong-password-checker-ii

class Solution:
    def strongPasswordCheckerII(self, password) :
        lower = False
        upper = False
        dig = False
        spec = False

        n = len(password)
        if n >= 8:
            for i in range(n):
                if password[i].islower():
                    lower = True
                if password[i].isupper():
                    upper= True
                if password[i].isdigit():
                    dig=True
                if not password[i].isalnum():
                    spec=True
                if i<n-1 and password[i]==password[i+1]:
                    return False

            return lower and upper and dig and spec
        else:
            return False