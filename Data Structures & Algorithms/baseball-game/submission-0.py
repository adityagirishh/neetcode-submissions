class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res=[]
        for i in operations:
            if i not in ["+","C","D"]:
                res.append(int(i))
                print(res)
            if i=="+":
                res.append(res[-1]+res[-2])
                print(res)
            if i=="C":
                res.pop()
                print(res)
            if i=="D":
                res.append(res[-1]*2)
                print(res)
        return (sum(res))
            
        