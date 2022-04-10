class Solution:
    def calPoints(self, ops: List[str]) -> int:
        scores = []
        for ops in ops:
            if ops == "+":
                scores.append(scores[-1] + scores[-2])
            elif ops == "D":
                scores.append(scores[-1]*2)
            elif ops == "C":
                scores.pop()
            else:
                scores.append(int(ops))
                
        return sum(scores)