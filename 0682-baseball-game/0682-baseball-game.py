class Solution:
    def calPoints(self, operations: List[str]) -> int:

        result = []

        for operation in operations:
            if operation not in "+DC":
                result.append(int(operation))
            elif operation == "C":
                result.pop()
            elif operation == "D":
                result.append(result[-1] * 2)
            elif operation == "+":
                result.append(result[-1] + result[-2])
        
        return sum(result)
