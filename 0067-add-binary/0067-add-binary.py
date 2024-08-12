class Solution:
    
        
    
    def addBinary(self, a: str, b: str) -> str:
        
        def decimalToBinary(s):

            if s == 0:
                return "0"
            binls = [1]



            while(s>sum(binls)):
                binls.append(2*binls[-1])


            binary_ls = [0]*len(binls)

            def find_sum_combination(nums, target):
                nums.sort(reverse=True)  # Sort the list in descending order
                combination = []
                current_sum = 0

                for num in nums:
                    if current_sum + num <= target:
                        combination.append(num)
                        current_sum += num
                    if current_sum == target:
                        break

                return combination

            cmb = find_sum_combination(binls, s)




            for i in cmb:
                for j in range(len(binls)):


                    if i == binls[j]:
                        binary_ls[j] = 1



            bino = ""
            for i in binary_ls:
                bino += str(i)

            return bino
                
    
        def BinarytoDecimal(binstr):
            decode_list = []
            st = 1

            for i in range(len(binstr)-1,-1,-1):
                decode_list.append(int(binstr[i])*st)
                st = 2*st

            return sum(decode_list)
        
        
        
        
        
        c = int(BinarytoDecimal(a))
        d = int(BinarytoDecimal(b))

        sumb = c + d

        return decimalToBinary(sumb)
    
