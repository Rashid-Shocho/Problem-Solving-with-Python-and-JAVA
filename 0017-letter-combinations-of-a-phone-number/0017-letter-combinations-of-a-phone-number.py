class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict1 = {"2":['a','b','c'], "3":['d','e','f'], "4":['g','h','i'], "5":['j','k','l'], "6":['m','n','o'], "7":['p','q','r','s'], "8":['t','u','v'], "9":['w','x','y','z']}

        op_list = []



        if len(digits) == 0:
            return ([])

        if len(digits) == 1:
            return (dict1[digits[0]])
        
        
        def combine_list(l1, l2):
            rt_list = []
            for i in range(len(l1)):
                for j in range(len(l2)):
                    rt_list.append(l1[i]+l2[j])
            return rt_list
        

        if len(digits) == 2:
            return (combine_list(dict1[digits[0]], dict1[digits[1]]))
       


        if len(digits)>2:
            c = len(digits)
            op_list = (combine_list(dict1[digits[0]], dict1[digits[1]]))
            for i in range(2,c):
                op_list = (combine_list(op_list, dict1[digits[i]]))
            return (op_list)


    

        