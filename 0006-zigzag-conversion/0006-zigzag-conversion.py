class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        res = [[] for _ in range(numRows)]

        direction = "down"

        i, j = 0, 0
     
        for j in range(len(s)):
            while i < numRows:
                res[i].append(s[j])

                if i == numRows - 1:
                    direction = "up"
                if i == 0:
                    direction = "down" 

                if direction == "down":
                    i += 1
                else:
                    i -= 1 
                break 
        
        def traverse_to_string(matrix):
            str = ""

            for row in matrix:
                for char in row:
                    str += char
        
            return str


        str = traverse_to_string(res)
        return str