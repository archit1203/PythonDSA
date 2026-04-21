class Solution:
    def isPalindrome(self, x: int) -> bool:
        val=str(x)
        val=val[::-1]
        if val==str(x):
            return True
        else:
            return False