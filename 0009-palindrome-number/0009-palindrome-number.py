class Solution:
    def isPalindrome(self, x: int) -> bool:
      a = str(x)
      b = a[len(a)-1:0:-1]
      b+=a[0]
      if a == b:
        return True
      else:
        return False