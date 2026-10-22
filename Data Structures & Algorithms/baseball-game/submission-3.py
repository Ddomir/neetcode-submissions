class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []

        for o in operations:
            if o == "+":
                scores.append(scores[-1] + scores[-2])
            elif o == "D":
                scores.append(2 * scores[-1])
            elif o == "C":
                scores.pop()
            else:
                scores.append(int(o))
        
        return sum(scores)