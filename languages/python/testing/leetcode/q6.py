class Solution:
    def convert(self, s: str, numRows: int) -> str:
        pass
        i = 0
        y_add = 0
        x_add = 0
        x = 0 
        y = 0
        one_base_index = i + 1
        for s_i in s:
            y = y + y_add
            x = x + x_add
            print(x,y)
            y_add = 1 if (i//(numRows-1))%2 == 0 else -1 

            if i%(numRows + numRows -2) < numRows -1:
                x_add = 0
            else: 
                x_add = 1
            i = i + 1
            one_base_index = i + 1
            

S = Solution()
S.convert("123456789012345",4)
             
