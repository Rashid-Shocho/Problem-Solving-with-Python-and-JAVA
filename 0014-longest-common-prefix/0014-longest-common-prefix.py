class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:       
        pre = ""
        count = 0
        flag = False
        for i in range(len(strs[0])):

            if flag:
                break
            var = strs[0][i]
            
            for j in range(len(strs)):
                try:
                    if strs[j][i] == var:
                        count+=1
                        
                    else:
                    
                        flag = True
                        break
                    if count==len(strs):
                        pre+=strs[j][i]
                        count = 0
                except:
                    flag = True
                    break
                
        return (pre)   