class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ls = []
        strg = ""
        for i in digits:
            strg+=str(i)
        strg = int(strg) + 1
        strg = str(strg)
        for i in strg:
            ls.append(int(i))
        return ls
        