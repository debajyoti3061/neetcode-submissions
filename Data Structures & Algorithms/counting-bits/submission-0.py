class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(n+1):
            temp = 0
            while (num):
                temp += num%2
                num = num >> 1
            res.append(temp)
        return res

                    
        