class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        ternary = []
        while(n>0):
            n, mod = divmod(n, 3)
            ternary.append(mod)
        s = list(set(ternary))
        ones = s.count(1)
        zeros = s.count(0)
        if ones > 0 and (len(s)-ones-zeros) == 0:
            return 'true'
        else: 'false'