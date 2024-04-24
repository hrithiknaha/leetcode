class Solution:
    def calPoints(self, operations: List[str]) -> int:

        result = []

        while operations:
            operation = operations.pop(0)

            if operation not in "+DC":
                result.append(int(operation))
            elif operation == "C":
                result.pop()
            elif operation == "D":
                val = result.pop()
                result.append(val)
                result.append(2*val)
            elif operation == "+":
                val1 = result.pop()
                val2 = result.pop()
                result.append(val2)
                result.append(val1)
                result.append(val1 + val2)
        
        sum = 0
        
        for num in result:
            sum += num
        
        return sum