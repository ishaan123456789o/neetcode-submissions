class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stck = []
        for op in operations:
            if op == '+':
                num1 = stck[-1]
                num2 = stck[-2]
                stck.append(num1 + num2)
            elif op == 'D':
                curr = stck[-1]
                stck.append(curr * 2)
            elif op == 'C':
                stck.pop()
            else:
                stck.append(int(op))
        return sum(stck)
        